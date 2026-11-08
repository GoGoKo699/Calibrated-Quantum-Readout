"""Direct Born-rule, full-tangent and complete-record checks for paid calibration.

Analytical statements and task restrictions are in science/paid-calibration.md.
Zero-probability outcomes contribute zero to ordinary pointwise score FI.
"""
import itertools, json
from pathlib import Path
import numpy as np
from math import comb
from readout import calibrated_effects

def povm(U):
    effects = calibrated_effects(3, 2)
    return np.array([U @ effect @ U.conj().T for effect in effects])

def fi(b, delta, rotation):
    U = np.eye(3)
    c, s = np.cos(delta), np.sin(delta)
    U[rotation, rotation] = U[2, 2] = c
    U[rotation, 2], U[2, rotation] = s, -s
    p, d = stats(povm(U), b)
    I = info(p, d)
    J = np.array([1 / ((1-b)*b), 4, 4, 4/(1-b), 4/(1-b), 4/b, 4/b])
    return I, I / np.sqrt(J[:, None] * J[None, :])

def tangents():
    out=[np.diag([1,-1,0]).astype(complex)]
    for i,j in [(0,1),(0,2),(1,2)]:
        for z in [1,1j]:
            x=np.zeros((3,3),complex); x[i,j]=z; x[j,i]=np.conj(z);out.append(x)
    return np.array(out)
X=tangents()

def stats(E,b):
    p=np.einsum('zij,ji->z',E,np.diag([1-b,b,0])).real
    d=np.einsum('zij,kji->zk',E,X).real
    return p,d

def info(p,d):
    # Exact selected settings can have a dark outcome. Drop floating-point
    # remnants only after checking its first derivative vanishes.
    keep=p>1e-15
    assert np.max(np.abs(d[~keep]), initial=0) < 1e-12
    return d[keep].T@(d[keep]/p[keep,None])

def conditional(delta):
    U=np.eye(3);c=np.cos(delta);s=np.sin(delta)
    U[0,0]=U[2,2]=c;U[0,2]=s;U[2,0]=-s
    return povm(U)

def check_transcript(b,m=2,n=2):
    e=np.eye(3);vectors=[(e[0]+e[2])/np.sqrt(2),(e[0]-e[2])/np.sqrt(2),e[1]]
    P=np.array([np.outer(v,v) for v in vectors]);p,d=stats(P,b)
    chain=m*info(p,d);direct=np.zeros((7,7));mass=0
    for y in itertools.product(range(3),repeat=m):
        py=np.prod(p[list(y)]);sy=np.sum(d[list(y)]/p[list(y),None],axis=0)
        l=sum(j!=2 for j in y);D=(y.count(0)-y.count(1))/l if l else 0
        delta=-np.arcsin(D)/2;q,dq=stats(conditional(delta),b)
        chain+=n*py*info(q,dq)
        for zs in itertools.product(range(10),repeat=n):
            if any(q[z]<=1e-15 for z in zs):continue
            prob=py*np.prod(q[list(zs)]);score=sy+np.sum(dq[list(zs)]/q[list(zs),None],axis=0)
            mass+=prob;direct+=prob*np.outer(score,score)
    err=float(np.max(np.abs(direct-chain)));assert err<1e-10
    assert abs(mass-1)<1e-12
    return {'b':b,'m':m,'n':n,'enumerated_possible_records':3**m*10**n,'chain_matrix_max_residual':err,'probability_mass':mass}

def check_formulas():
    errs=[]; cases=0
    for b in [1e-10,1e-6,.01,.3]:
      a=1-b
      for delta in [-.4,-.1,-.01,0,.01,.1,.4]:
        c=np.cos(delta);s=np.sin(delta);t=np.sin(2*delta)
        _,Hs=fi(b,delta,0);_,Hw=fi(b,delta,1)
        A=b+a*c*c;B=b+a*s*s
        rs=b/4*(c*c/B+s*s/A)
        real=np.cos(2*delta)**2/(4*(1+t)*(1-t/2))+b*c*c*s*s/2*(1/(a+b*c*c)+1/(a+b*s*s))
        imag=1/(4*(1-t/2))
        v=np.array([c,-s]);w=np.array([s,c]);D=np.diag([1,np.sqrt(b)])
        block=D@(np.outer(v,v)/A+np.outer(w,w)/B)@D/4
        errs.extend([abs(Hs[5,5]-rs),abs(Hs[6,6]-rs),abs(Hw[5,5]-real),abs(Hw[6,6]-imag),np.max(abs(Hs[np.ix_([1,5],[1,5])]-block)), np.max(abs(np.linalg.eigvalsh(Hs[np.ix_([2,6],[2,6])])-np.linalg.eigvalsh(block)))]);cases+=1
    err=float(max(errs));assert err<1e-12
    for b in [.3,.01,1e-10]:
      _,H=fi(b,0,0); assert np.max(abs(H-np.diag([.5]+[.25]*6)))<1e-12
    limits=[]
    for delta in [-.4,-.1,.1,.4]:
      b=1e-10;u=np.sin(2*delta)
      _,H=fi(b,delta,1)
      expected=np.sort([.5,.25,.25,.25,.25,(1-u)/(4*(1-u/2)),1/(4*(1-u/2))])
      residual=float(np.max(abs(np.linalg.eigvalsh(H)-expected)))
      assert residual<2e-5
      limits.append({'delta':delta,'b':b,'limit_eigenvalue_residual':residual})
    return {'cases':cases,'max_residual':err,'exact_calibration_matrices':3,'weak_error_limit_checks':limits}

def binomial_fraction(b, m):
    a = 1-b
    value = 0.0
    for ell in range(m+1):
        for k in range(ell+1):
            D = (2*k-ell)/ell if ell else 0
            probability = comb(m, ell)*a**ell*b**(m-ell)*comb(ell,k)/2**ell
            value += probability*(b/4)*(1-a*D**2/2)/(b+a*a*D**2/4)
    return value

def check_pilot_mixture():
    checks = []
    for b in [.01, .2]:
        m=2
        e=np.eye(3)
        P=np.array([np.outer(v,v) for v in [(e[0]+e[2])/np.sqrt(2), (e[0]-e[2])/np.sqrt(2), e[1]]])
        p,_=stats(P,b)
        direct=0.0
        for y in itertools.product(range(3),repeat=m):
            ell=sum(j!=2 for j in y)
            D=(y.count(0)-y.count(1))/ell if ell else 0
            _,H=fi(b,-np.arcsin(D)/2,0)
            direct += np.prod(p[list(y)])*H[5,5]
        error=abs(direct-binomial_fraction(b,m))
        assert error<1e-13
        checks.append({'b':b,'m':m,'direct_vs_binomial_residual':float(error)})
    b=1e-12
    even_limit=comb(4,2)/(4*2**4)
    assert abs(binomial_fraction(b,4)-even_limit)<1e-10
    assert binomial_fraction(b,3)<1e-10
    return {'mixture_checks':checks,'even_m4_limit':even_limit,'evaluated_even_m4':binomial_fraction(b,4),'evaluated_odd_m3':binomial_fraction(b,3)}

def pd_pilot():
    effects=[];eye=np.eye(3,dtype=complex)
    for i,j in [(0,1),(0,2),(1,2)]:
      k=3-i-j
      for z in [1,1j]:
        for v in [(eye[i]+z*eye[j])/np.sqrt(2),(eye[i]-z*eye[j])/np.sqrt(2),eye[k]]:
          H=np.outer(v,v.conj())/6
          effects.append(.8*H+.2*np.trace(H).real*np.eye(3)/3)
    return np.array(effects)

if __name__=='__main__':
    data={'formula_checks':check_formulas(),'transcript_checks':[check_transcript(b) for b in [.01,.2]],'pilot_mixture':check_pilot_mixture(),'pd_pilot':[]}
    for b in [1e-2,1e-4,1e-6]:
      effects=pd_pilot();assert np.max(abs(effects.sum(axis=0)-np.eye(3)))<1e-12
      p,d=stats(effects,b);assert p.min()>=.2/18-1e-15;I=info(p,d)
      assert (1-b)**2*I[3,3]>.4 and 3<I[5,5]<3.3
      data['pd_pilot'].append({'b':b,'strong_angular_FI':float((1-b)**2*I[3,3]),'weak_angular_FI_over_b_squared':float(I[5,5])})
    Path(__file__).with_name('paid-calibration-results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
