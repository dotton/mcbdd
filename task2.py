import matplotlib.pyplot as plt
import numpy as np


# Define the events D = {patient has disease}, H = {p is healthy},
# P = {p has positive test}, N = {p has negative test}.
#
# We have by definition
#  P(D|P) = P(D,P) / P(P) = P(P|D)*P(D) / P(P)
#
# with
#  P(P) = P(P,D) + P(P,H) = P(P|D)*P(D) + P(P|H)*P(H)
#       = P(P|D)*P(D) + (1-P(N|H))*(1-P(D)),
#
# where P(D) = prevalence, P(P|D) = sensitivity, P(N|H) = specifity.
def p_D_given_P(sensitivity, specifity, prevalence):
    p_D_and_P = sensitivity * prevalence
    p_P_and_H = (1-specifity) * (1-prevalence)
    p_D_given_P = p_D_and_P / (p_D_and_P + p_P_and_H)
    return p_D_given_P


fig, ax = plt.subplots()

prevalences = np.arange(0.0001, 0.5, 0.0001)
specifities = set([0.99, 0.999, 0.9999, 0.99999]) 
sensitivity = 0.99
for specifity in specifities:
    plot_data = {}
    plot_data[specifity] = []
    for prevalence in prevalences:
        p = p_D_given_P(sensitivity, specifity, prevalence)
        plot_data[specifity].append(p)

    ax.plot(prevalences, plot_data[specifity], label="specifity = "+str(specifity))

plt.title("Probability of infection given a positive test with sensitivity = " + str(sensitivity))
plt.ylabel("P(D|H)")
plt.xlabel("Prevalence")
plt.legend(loc="lower right")

plt.show()


# Example in numbers:
# For a prevalence of 0.01, a specifity of 0.99 and a sensitivity of 0.99, P(D|P) = 0.5
#
# We check the result with integer numbers with n = |D or H| = 100'000 people. We have:
# |D| = 100, |H| = 9900, 
# |D and P| = 99, |D and N| = 1
# |H and N| = 98901, |H and P| = 99
# |P| = |D and P| + |H and P| = 198, |N| = 9802
#
# This gives a P(D|P) = |D and P|/|P| = 99/198 = 0.5
