import numpy as np 

def ortho(a):
    q = []
    for x in a:
        q_curr = x
        for q_i in q:
            print('dot \n', np.dot(q_i.T, x))
            print('term \n',  q_i)
            q_curr -= np.dot(q_i.T, x) * q_i

        # print(a[x], q_curr)
        print('unnormalised \n', q_curr)
        q_curr = q_curr/np.linalg.norm(q_curr)
        print('normalised \n', q_curr)

        q.append(q_curr)
        print('_________')

    for q_ in q:
        print(q_)


a1 = np.zeros((5, 1))
a1[0] = -1
a2 = np.zeros((5, 1))
a2[0] = -1
a2[1] = -1
a3 = np.zeros((5, 1))
a3[0] = -1
a3[1] = -1
a3[2] = -1
a4 = np.zeros((5, 1))
a4[0] = -1
a4[1] = -1
a4[2] = -1
a4[3] = -1
a5 = np.zeros((5, 1))
a5[0] = -1
a5[1] = -1
a5[2] = -1
a5[3] = -1
a5[4] = -1

# a = [a1, a3, a5, a2, a4]
# a = [a1, a2, a3, a4, a5]
a = [a5, a4, a3, a2, a1]
for x in a:
    print(x)
print('________________')
ortho(a)