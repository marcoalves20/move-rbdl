import rbdl
import numpy as np
import matplotlib.pyplot as plt
def get_joint_pos(X_base):
  return np.stack([joint.r for joint in X_base], axis=0)


# Create a new model
model = rbdl.loadModel('track00_model.urdf')
state = np.zeros(model.q_size)
state[-4:] = 1.0

rbdl.UpdateKinematics(model, state, np.zeros(model.q_size), np.zeros(model.q_size))
pose = get_joint_pos(model.X_base)

# make a 3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pose[:,0], pose[:,1], pose[:,2])
#set axis limits
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
plt.show()