import pytearcat as pt

t, r, theta, phi = pt.coords('t,r,theta,phi')
k, c = pt.con('k', 'c')

a = pt.fun('a', 't')

ds = 'ds2 = -dt**2 + a**2 * (1/(1 - k*r**2)*dr**2 + r**2 * dtheta**2 + r**2*sin(theta)**2 * dphi**2)'

g = pt.metric(ds)


Ch = pt.christoffel()
Ch.display()

R = pt.riemann(All=True)
print(R.display("^,_,_,_"))


