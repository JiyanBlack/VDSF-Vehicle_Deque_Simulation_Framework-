from Objects.Vehicle import Vehicle


class CAV(Vehicle):
    def __init__(self, idx, model, simulationStep, v_intend, leader=None):
        super().__init__(idx, leader, simulationStep, max_v=v_intend)
        self.tsys = 0.5  # system response time setting for autonomous vehicles in eq6
        self.model = model
        self.vi = self.max_v  # intended speed in m/s, not km/h
        self.comfort_acc = 1  # comfort acceleration
        self.comfort_dec = -1  # comfort deceleration
        self.max_acc = 2  # maximum acceleration capacity
        self.max_dec = -3  # maximum deceleration capacity
        self.braking_signal = False  # if receive braking signal, re
        self.response_time_braking = 0

    def update(self):
        self.base_update()
        if self.maxBraking:
            new_a = self.max_dec
            new_v = self.v + new_a * self.simulationStep / 1000
        else:
            new_a = self.model.get_acc(self)
            new_v = self.v + new_a * self.simulationStep / 1000
        if new_v < 0:
            new_v = 0
            new_a = (new_v - self.v) * 1000 / self.simulationStep
        new_loc = self.loc + new_v * self.simulationStep / 1000
        self.a = new_a
        self.v = new_v
        self.loc = new_loc
