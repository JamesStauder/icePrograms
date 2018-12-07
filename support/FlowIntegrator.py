from scipy.integrate import ode
import numpy as np


'''
Class: FlowIntegrator
Integration class developed my Jake Downs. 


Dependencies: scipy ode
Creator: Jake Downs
Date created: Unknown
Last edited: 3/2/18
'''


class FlowIntegrator:
    def __init__(self, vxDataSet, vyDataSet):

        self.vxDataSet = vxDataSet
        self.vyDataSet = vyDataSet

        # Velocity right hand side function
        def rhs(t, u):
            x = u[0]
            y = u[1]
            d = u[2]

            vx = vxDataSet.getInterpolatedValue(x, y)
            vy = vyDataSet.getInterpolatedValue(x, y)
            v_mag = np.sqrt(vx**2 + vy**2)
            return np.array([-vx / v_mag, -vy / v_mag, v_mag])

        # ODE integrator
        self.integrator = ode(rhs).set_integrator('vode', method = 'adams')

    # Set the currently displayed data field
    def integrate(self, x0, y0, flowline, indexMarker, resolution):
        u0 = np.array([x0, y0, 0.])
        self.integrator.set_initial_value(u0, 0.0)

        # Approximate spacing in m between points (depends on actual flow path)
        spacing = resolution
        dist_mult = 1.0
        # time step
        dt = spacing / dist_mult

        # vx and vy at current location
        vx = self.vxDataSet.getInterpolatedValue(x0, y0)
        vy = self.vyDataSet.getInterpolatedValue(x0, y0)

        v_mag = np.sqrt(vx**2 + vy**2)

        # x and y positions along flow line
        xs = [x0]
        ys = [y0]
        # Distance traveled
        ds = [0.0]
        # times
        ts = [0.]

        count = indexMarker
        
        while self.integrator.successful() and count < len(flowline)-1:
            count = count + 1

            # Step forward
            u = self.integrator.integrate(self.integrator.t + dt)

            # Update v mag to check stopping condition
            x = u[0]
            y = u[1]
            d = u[2]

            flowline[count] = [x, y]

            xs.append(x)
            ys.append(y)
            ds.append(d)
            ts.append(self.integrator.t)
            vx = self.vxDataSet.getInterpolatedValue(x, y)
            vy = self.vyDataSet.getInterpolatedValue(x, y)
            v_mag = np.sqrt(vx**2 + vy**2)

        return flowline


