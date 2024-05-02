#!/usr/bin/env python
# coding: utf-8

# # Mathematical Model of an Armaments Race 
# 
# ---
# 

# # Background and Motivation

# The motiation of an arms race between countries is to be the superiorly armed force that has access to the latest weapons and technologies. The simplest depiction of an arms race is a conflict between two nations, cause by political, cultural, economic or some other tensions. The arms race must always consist of some notion of retaliation. If both sides were not increasing their arms, there would be no race. The Cold War could be regarded as the ideal arms race example due to the immense acquisition of material and innovation expenditure for both nations (Wallace, M.D (1979)). Post World War 2, the United States and the Soviet Union, once allies, turned sour due to conflicting geopolitical perspectives. The arms race was on and neither side was going to back down. The Soviet Union spent approximately 27% of their GDP on its military, and the United States around 8 trillion USD. Around 90% of all nuclear warheads worldwide are currently held by Russia and the US. However, despite Russia's 6257 nuclear warheads, the Cold War left the country in a financial crisis, even worse than the Great Depression ("History.com, Arms Race,").
# 
# The consequences of war can be devastating to the livelihoods of the people involved. Countless innocent lives are displaced or lost due to unsanctioned, deadly acts perpetrated by aggressive nations and politics. For institutes and governments whose goal is to provide the best conditions for the world or for the people of their country's, understanding the dynamics of military expenditures is of the utmost importance. For defence contractors who spend billions of dollars globally and are awarded billions of dollars in contracts, predicting when countries will spend more money is just good business. In 2020, world military expenditures rose to 1.98 trillion USD according to the Stockholm international peace institute (SIPRI) (Watson.brown.edu, Costs of War) and global expenditures are expected to surpass 2 trillion USD in 2022. However, arms and military services spending cannot grow exponentially without some undesirable implication on the economic growth of that country. While defence spending can create jobs and promote growth through the spending of government resources, military spending is generally thought to have negative effects on the economy as the opportunity costs outweigh the benefits of increased government spending.
# 
#   We focus on the arms race perpetrated by the civil war between North and South Korea as it is a direct consequence of the Cold War. Due to Soviet influence in the growingly independent North Korea, there arose anti-West propaganda which opposed the Western-influenced South Korean government. Their differing political stances lead to the North invading the South - a war that lasted three years and claimed 2.8 million lives ("Effects of the Cold War," n.d). 
#   
#   The tension produced by North Korea the past 50 years is palpable. North Korea has committed themselves into a hyper-militarized structure that has channelled billions of dollars into weapons of mass destruction ("Britannica, Arms Race"). The United Nations Security Council (UNSC) has invoked sanctions to deter North Korea’s ballistic missile program, yet reports of nuclear testing are still undergoing. North Korea’s denuclearization is still a concern for the international community and unfortunately, sanctions appear to not hinder their progress. As it stands North Korea’s anti-Western propaganda is an immediate threat to South Korea and visualizing the influence both nations have on each other holds insight into the geopolitical stability of every nation involved.

#  # Research Question

# In an arms race between North and South Korea, how does their armaments spending and the feelings of animosity between each country influence each of their military spending? In addition, consider the addition of the United States to the arms race between North and South Korea. How does the United States' military spending and the general sentiments between each country influence the military expenditures of all three countries?

# # Base Model Construction

# To answer the question of how armament spending of both North and South Korea and their mutual feelings influences their future spending, we begin with the Richardson Model for Armament Races (Gillespie 1975). The Richardson model relates two antagonistic nations' arms and military services spending to eachother via the pair of ordinary linear continuous time differential equations.
# 
# The Richardson Model for Armament Races, adapted for the arms race between North and South Korea, is built upon three underlying assumptions about the nature in which these two antagonistic countries will increase or decrease their armaments. The first follows that out of fear of military insecurity, North Korea will increase its armaments expenditures proportional to the level of expenditures of South Korea and similarily, South Korea will increase their military expenditures proportional to the level of expenditures of North Korea. Second, we assume that increased armaments spending poses an economic burden on the economy such that it degrades the health of the countries economy and restrains further military spending by some proportion of the current spending. Third, we suppose some hostilities or grievances between two countries remain constant over time and are independent of the levels of military threats brought on by the military expenditures of other countries (Gillespie 1975). Here, we assume that North and South Korea are antagonistic countries such that there is absolutely no overall good will between them.
# 
# We find support for the latter two assumptions in the literature. Well summarized by Heliyon (2020), military expenditures "tend to attenuate productivity because more funds diversion to military expenditure causes the government to either increase taxes or get loans from the foreign capital market to balance its budget. The second alternative is therefore primarily harmful to economic prosperity, since it escalates the rate of interest, decreases investment and consumer demand and drives sluggish economic growth" (Azam 2020). Similar views are taken by other authors who note that military expenditures are harmful to the growth of any economy (Lim 1983) and that at best, military expenditures provide no positive influence on economic growth (Dunne 2000). Largely, these negative influences on economic growth come by means of opportunity costs where diverted spending to military services prevents spending in other sectors (Bhattacharjee and Mazumdar 2018). To support the notion that North and South Korea are antagonistic countries, we take the results of a 2014 BBC poll which found on 3% of South Koreans looked positively towards their Northern neighbours while a staggering 91% of South Koreans expressed negative view of North Korea (2014). Similarily we take North Korea's repeated comments of South Korea that the North views the South in a negative light (van der Meer 2011).
# 
# In light of these remarks, we introduce the parameters of the Richardson Model of Armament Races. We let $x$ represent the annual arms expenditures of North Korea while $y$ represents the annual arms expenditures of South Korea, both in units of USD. Since we assume that one country will want to increase its military spending by a proportion of the other country's military spending, we define the following proportionality constants, $a$ and $b$, both of which are given in units of $year^{-1}$. The parameter $a$ represents the proportion of South Korea's military expenditures which North Korea's increase by and $b$ is the proportion that the South's increase by in response to the North's expenditures. The parameters $m$ and $n$ represent the economic burden imposed by the level of armament spending of North and South Korea, respectively, and are given in units of $year^{-1}$. Finally, the parameters $r$ and $s$ encompass the assumption that North and South Korea are antagonistic and will have some baseline feelings of grievance towards one another. The parameter $r$ is the level of grievance felt by the North towards South Korea and $s$ the level of grivance felt by the South towards North Korea. Both $r$ and $s$ are given in units of $\frac{USD \; in \; millions}{year}$.
# 
# We now introduce the Richardson Model of Armaments Races in the form of two coupled linear differential equations, written in terms of the parameters stated above:
# 
# 
# $$\frac{dx}{dt} = ay - mx + r$$
# 
# $$\frac{dy}{dt} = bx - ny + s$$
# 
# 
# The two differential equations describe the change in military expenditures of North Korea ($\frac{dx}{dt}$) and South Korea ($\frac{dy}{dt}$) in units of millions of USD per year. The decision to create a continous time model was primarily based on the fact that  military spending and the influences of military spending occur at all times of the year and are constantly beign reassessed and re-evaluated by different countries.
# 
# We recognize that the Richardon model provides some excessive simplification of a justafiably complex dynamic between two antagonistic countries with military budgets in the billions of dollars. The first assumption we make relies on the notion that a country will change its arms spending as a proportion of the other countries absolute military spending. This may be an adequate assumption for two comparably sized and well developed militaries whcih are comparably matched but South Korea currently spends approximately thirty times more than North Korea on its military (2022). Therefore, South Korea may not feel the necessity to spend to increase their military spending if they already feel more capable than North Korea. Similarily, North Korea may feel the need to catch up and increase their military spending more considerably for a short period and then less so in later years, suggesting the $a$ and $b$ parameters should not be constant. Similarly, we cannot necessarily assume grievances held between countries remain fixed over time. One country may provoke the other, raising tensions between the two countries before they settle down for sometime, suggesting the assumption that the $r$ and $s$ parameters are constant is too much of a simplification. Therefore, after the analysis of this Richardson Model for Armament Races, we propose two further extensions on this model to address some of these concerns, and further address our research question.
# 
# In a search of the literature, we found a range of parameters for the Richardson Model of Armament Races which were used to describe the arms race between two countries in a number of situations: where both countries were attacking eachother, where one country was the primary aggressor and where both countries were stockpiling arms as a means of deterrance. However, the arms race between North and South Korea does not appear to have been examined. Since neither North or South Korea engaged in any recent active conflict, we treat both countries as attempting to deter the other country from engaging in an active conflict and examine a range of parameters for the model of North and South Korea's future military spending.
# 
# South Korea's military expenditures are much greater than those of North Korea (2022) and that North Korea's military began growing at faster rates many decades after South Korea's military had modernized (United States. Defense Intelligence Agency). It seems that North Korea is playing catch up with their military expenditures compared with the arms expenditures of their neighbouring antagonistic countries such as South Korea. While South Korea's much greater military spending may suggest the North could only increase their spending by a much smaller proportion compared to the South, the North's desire to catch their military spending up the thatof the South may suggest otherwise. But, given North Korea's seeminlgy strong desire to catch-up their military spending, we assume they will increase their military spending by a slightly greater proportion of South Korea's expenditures than South Korea will of the North's military expenditures. In the literature, we find that the proportionality constants of the model are usually in the range of 0.25 to 0.55. Thus, we model a range of the parameters $a$ and $b$ take the values 0.3 and 0.25 or 0.45 and 0.4, in units of $year^{-1}$.
# 
# Subsequently, we examine a possible range of parameters for $m$ and $n$, which take into account the limiting influence of current military spending on future expenditures. Since North Korea is on eof the poorest countries globaly (2018), we expect any military spending of North Korea to be a greater economic burden on North Korea than on South Korea. Therefore, we believe $m$ will take larger values than $n$, and examine the following range of parameters: $m$ and $n$ are either 0.35 and 0.25 or 0.4 and 0.3, in units of $year^{-1}$. 
# 
# Finally, previous research by the BBC (2014) shows that both North and South Korea view eachother in a negative light, thus we let both $r$ and $s$ take on the values of 4000 $\frac{million \; USD}{year}$. 
# 
# The combination of these parameters results in four possible trajectories which are plotted below (Fig. 1). Each of these trajectories are plotted from the current military expenditures of North and South Korea. For convenience, these four models are written out below, labelled 1 through 4:
# 
# \begin{align}
# \frac{dx}{dt} &= 0.3y - 0.35x + 4000 \tag{1} \\
# \frac{dy}{dt} &= 0.25x - 0.25y + 4000 \\
# \frac{dx}{dt} &= 0.3y - 0.4x + 4000 \tag{2} \\
# \frac{dy}{dt} &= 0.25x - 0.3y + 4000 \\
# \frac{dx}{dt} &= 0.45y - 0.35x + 4000 \tag{3} \\
# \frac{dy}{dt} &= 0.4x - 0.25y + 4000 \\
# \frac{dx}{dt} &= 0.45y - 0.4x + 4000 \tag{4} \\
# \frac{dy}{dt} &= 0.4x - 0.3y + 4000
# \end{align}

# # Base Model Analysis

# To answer how each of North and South Korea's current military spending influences each countries future military spending, we look at the long-term behaviours of the the model. We simulate the behaviours of the model under the four variations of parameters described above. We also analytically determine the existence of any equilibrium along with the stability of any equilibrium.  These analyses enable a mathematical description of the long-term trends of North and South Korea's military expenditures in an arms race between the two countries, whether the miltary expenditures of both countries increase unbounded or move towards some equilibrium value and the nature in which they approach the equilibrium value.
# 
# To show whether an equilibrium exist for the Richardson Model of Armaments Races exist under the variations of paramters chosen above, we look for the existence of fixed points by determining where the change in spending of both countries is equal to zero ($\frac{dx}{dt}=\frac{dy}{dt}=0$). Since we assume all the parameters are greater than zero, it can be shown that the sole fixed point of all the model exists at:
# 
# $$ x_0 = \frac{nr + as}{mn - ab}, y_0 = \frac{br + ms}{mn - ab}$$
# 
# Therefore, the first variation of the model (1) has an equlibrium fixed point where North Korea spends 176 000 million USD and South Korea spends 192 000 million USD. The other equations written above have equilibrium fixed points where North and South Korea annual military expenditures are (53 333 million USD, 57 778 million USD), (-30 270 million USD, -32 432 million USD) and (-50 000 million USD, -53 333 million USD), for variations in the parameters labelled 2, 3, and 4, respectively.
# 
# Subsequently, we determine the stability of these fixed point to show whether the military expenditures of the two countries will move toward or away from these values, oscillate around them in some way, or some combination of both. We use the trace-determinant plane, a reliable way to determine the stability and nature of that stability of a multivariate continuous time systems. We first find the Jacobian matirx A, which is shown below:
# 
# \begin{bmatrix}
#     -m & a \\
#     b & -n 
# \end{bmatrix}
# 
# The trace of A and the determinant of A are shown below:
# 
# $$tr(A) = -m-n$$
# 
# $$det(A) = mn - ab$$
# 
# Since all the parameters are positive, the trace is always less than zero. Therefore the model will have a stable fixed point when the determinant is greater than zero, in other words when $mn > ab$. Under the variations in parameters in equations (1-4), it can be shown that the determinant is greater than zero for only the systems of equations labelled (1) and (2) above. For the model parameters shown in the system of equations (3) and (4), the determinant of the Jacobian is less than zero, indicating a semi-stable equilbrium. We ignore the variations in parameters (3) and (4) from here on out because they lead to negative annual spending, which is not realistic in the real world, and does not satisfy conditions for out model. For the stable equilibrium points in (1) and (2), we further investigate the type of sink the stable fixed points of the model are. If the expression shown below is greater than zero, the fixed point is a spiral source, which indicates the expenditures of each country should exhibit damped oscillations, otherwise we do not expect to see oscillatory behaviour about the fixed points.
# 
# $$ tr(A)^{2} - 4 \: det(A)$$
# 
# For the variations of parameters shown in (1), the expression evaluates to greater than zero, indicating the stable equilibrium point is a nodal sink, where the spending of both countries will trend towards. Similarily, the expression evaluates to greater than zero for the parameters shown in (2). Therefore with the parameters given in the system of equations (2), the equations will also trend towards the equilibrium fixed point without showing any kind of fluctuations or oscillations in spending and can be classified as a nodal sink.
# 
# One way to conceptualize the meaning of this analysis is to think in terms of the countries willingness to grow their armaments compared to their willingness to grow their economy. If the two countries have a greater economic burden caused by their military expenditures than their willingness to grow their military spending ($mn > ab$), then the countries spending will tend to a stable fixed point described above for parameter variations (1) and (2).
# 
# For variations in parameters (3) and (4), we find the results suggest our model is oversimplified resulting in assumption being false. For example, the idea that both antagonistic countries want to increase their arms spending as a proportion of the other's absolute spending, or that military spending negatively impacts economic health, therefore dampening further economic spending could be false assumptions. Or, maybe the influence of countries outside of North and South Korea play an important role in their arms race. Nevertheless, annuals spending cannot be less than zero
# 
# Below, we show a simulation of North Korean and South Korean military spending over the next 1000 years, beginning at the curreent levels of spending, 1.6 billion USD for North Korea and 47 billion USD for South Korea (UNSC 2022). We plot thew model for both the variations in parameters (1) and (2) on a vector field and the expenditures as a function of time.

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def base_model(mod, params, t, X0, xmax, ymax, xmin,ymin):
  X = integrate.odeint(mod, X0, t, args=params)

  n_points = 20
    
  x = np.linspace(xmin, xmax, n_points)
  y = np.linspace(ymin, ymax, n_points)
    
  X1, Y1 = np.meshgrid(x, y)
  DX1, DY1 = mod([X1, Y1], 0, params[0], params[1], params[2], params[3], params[4], params[5])
    
  M = (np.hypot(DX1, DY1))
  M[M == 0] = 1.
    
  DX1 /= M
  DY1 /= M

  
  return X, X1, Y1, DX1, DY1, M

def Richardson(X, t, a, b, m, n, r, s):
    x, y = X[0], X[1]
    return [a*y - m*x + r, b*x - n*y + s]

# initialize figure with four panels
fig, axs = plt.subplots(2,2)
xmax = 200000
ymax = 200000
X0 = [1600, 47000] # initial expenditures
t = np.linspace(0, 1000, 1000)



# plot trajectory 1
trajectory_1_a = 0.3
trajectory_1_b = 0.25
trajectory_1_m = 0.35
trajectory_1_n = 0.25
trajectory_1_r = 4000
trajectory_1_s = 4000


trajectory_1_x_fixed = (trajectory_1_n*trajectory_1_r+trajectory_1_a*trajectory_1_s)/(trajectory_1_m*trajectory_1_n-trajectory_1_a*trajectory_1_b)
trajectory_1_y_fixed = (trajectory_1_b*trajectory_1_r+trajectory_1_m*trajectory_1_s)/(trajectory_1_m*trajectory_1_n-trajectory_1_a*trajectory_1_b)

trajectory_1_params = (trajectory_1_a,trajectory_1_b,trajectory_1_m,trajectory_1_n,trajectory_1_r,trajectory_1_s)

X, X1, Y1, DX1, DY1, M = base_model(Richardson, trajectory_1_params, t, X0,xmax,ymax,0,0)

axs[0,0].quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.plasma)


axs[0,0].plot(X[:,0], X[:,1])
axs[0,0].plot(trajectory_1_x_fixed,trajectory_1_y_fixed,'ro')
axs[0,0].set_title("Trajectory 1")


# plot trajectory 2
trajectory_2_a = 0.3
trajectory_2_b = 0.25
trajectory_2_m = 0.3
trajectory_2_n = 0.4
trajectory_2_r = 4000
trajectory_2_s = 4000

trajectory_2_x_fixed = (trajectory_2_n*trajectory_2_r+trajectory_2_a*trajectory_2_s)/(trajectory_2_m*trajectory_2_n-trajectory_2_a*trajectory_2_b)
trajectory_2_y_fixed = (trajectory_2_b*trajectory_2_r+trajectory_2_m*trajectory_2_s)/(trajectory_2_m*trajectory_2_n-trajectory_2_a*trajectory_2_b)

trajectory_2_params = (trajectory_2_a,trajectory_2_b,trajectory_2_m,trajectory_2_n,trajectory_2_r,trajectory_2_s)

X, X1, Y1, DX1, DY1, M = base_model(Richardson, trajectory_2_params, t, X0,xmax,ymax,0,0)

axs[0,1].quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.plasma)
axs[0,1].plot(X[:,0], X[:,1])
axs[0,1].plot(trajectory_2_x_fixed,trajectory_2_y_fixed,'ro')
axs[0,1].set_title("Trajectory 2")

# plot trajectory 3
def fx(t, q, a,b,m,n,r,s):
    x, y = q
    return [a*y - m*x + r, b*x - n*y + s]

params = (0.3,0.25,0.35,0.25,4000,4000)
tp = [0,1000]

X = integrate.solve_ivp(fx,tp, X0, args=params, dense_output=True)

q = X.sol(t)

axs[1,0].plot(t,q.T[:,1],'r')
axs[1,0].plot(t,q.T[:,0],'k')
axs[1,0].legend(['North Korea','South Korea'], shadow=True)
axs[1,0].set_title("Trajectory 1 Expenditures Plotted Against Time")


# plot trajectory 4
params = (0.3,0.25,0.3,0.4,4000,4000)

X = integrate.solve_ivp(fx,tp, X0, args=params, dense_output=True)

q = X.sol(t)

axs[1,1].plot(t,q.T[:,1],'r')
axs[1,1].plot(t,q.T[:,0],'k')
axs[1,1].legend(['North Korea','South Korea'], shadow=True)
axs[1,1].set_title("Trajectory 2 Expenditures Plotted Against Time")

count = 0
for ax in axs.flat:
    if count < 2:
        ax.set(xlabel='North Korea Armament Expenditure (million USD/year)', ylabel='South Korea Armament Expenditure (million USD/year)')
        count += 1
    else:
        ax.set(xlabel='Years', ylabel='Armament Expenditure (million USD)')

fig.set_size_inches(16, 9)
fig.set_dpi(100)

plt.tight_layout()




# # Model Extensions

# ### First Model Extension Construction

# In the Richardson Model of Armament Races, there is an assumption that arms races occur solely between two countries. However, countries around the world rely on eachother in both times of peace and war for the defence of their sovereignty. While North and South Korea are the only two countries on the Korean peninsula, their economies and actions are intertwined with those of neighbouring coutnires and allie around the world. In terms of militaries, South Korea is a close ally of the United States, which spends the greatest amount on their military out of any country globally. Similar to the relationship between North and South Korea, North Korea and the United States view eachother in a negative light (2014). To improve upon the Richardson Model of Armament Races, we introduce the United States as a third country in the model, whose military expenditures influence the future military expenditures of both North and South Korea.
# 
# Referring back to the Richardson Model of Armament Races, we consider that the expenditures of each country will rise to some proportion of what the other countries spend. While the intuition ans support for this assumption is established above for two antagonistic countries, we also find it true of two allied countries. If the United States increases its military expenditures, we assume that it forecasts threats globally and will apply pressure to allied countries to raise their defence budgets as well.  This is supported by the rise in defence spending by all NATO countries in the past year (NATO 2022).
# 
# The assumption that a countries defence spending negatively impacts the health of its economy, therefore dampening further defence spending goes unchanged from the Richardson Model. Similarily, polling shows similar views in both the United States and South Korea towards North Korea, and comments exhibited by North Korea are similar towards both South Korea and the United States have been similar in nature (2014).
# 
# We introduce an extended variation of the Richardson Model for Armament Races which consists of three coupled differential equations. We let $x$, $y$, and $z$ represent the annual arms expenditures of North Korea, South Korea and The United States of America in USD. Subsequently, we let $a$, $b$, and $c$ for North Korea, South Korea and the United States, respectively. These parameters represent the proportion of harm done to each countries economy which inhibits future military expenditures, and is given in units of $year^{-1}$. We also define the parameters $g$, $h$, and $i$ for North Korea, South Korea and the United States. These parameters have units of $\frac{USD \; in \; millions}{year}$, and account for the general feelings of animosity and fear towards opposing countries. Lastly, the parameters $k$, $l$, and $m$ represent the proportion that a country will increase their military expenditures in accordance with the other countries expenditures. For simpicity, we treat the proportion that North or South Korea's miliatry spending is increased by the level of spending of the United States as the same, and extend this to the relation with both North and South Korea's expenditures as well. We let $k$ be the proportion a country increases their military expenditures due to North Korea's expenditures, $l$ be the proportion North Korea and the Unite States increase their expenditures due to South Korea's military expenditures and $m$ be the proportion of the United States expenditurs the Korea's increase their military expenditures by. The parameters $k$, $l$, and $m$ all have units of $year^{-1}$.
# 
# Therefore we introduce the Richardson Model of Armaments Races in the form of three coupled linear differential equations, written in terms of the parameters stated above:
# 
# $$\frac{dx}{dt} = -ax+ly+mz+g$$
# 
# $$\frac{dy}{dt} = −by+kx+mz+h$$
# 
# $$\frac{dz}{dt} = −cz+kx+ly+i$$
# 
# All the parameters and the variables $x$, $y$, and $z$ are considered to always be positive.
# 
# When considering parameters appropriate for the model, we take an approach similar to determining the parameters in the Richardson model. For the parameters $k$, $l$, and $m$, we consider the agressive rhetoric of North Korea. Therefore, we set the parameter $k$ as the highest value of these three parameters, at 0.38 $year^{-1}$. While North Korea may exhibit agressive rhetoric towards other countries, the same is not necessarily true of South Korea and the United States. We also see no reason to differentiate between $l$ and $m$. Therefore, we assign $l$ and $m$ the values 0.35 $years^{-1}$ each.
# 
# To account for the negative impact on economic health, these proportions will relate to the size of their exonomies, and larger economies will have the capacity to handle larger military expenditures with limited impairment to future spending. Thus $a$ is assigned 1.0 $year^{-1}$ for North Korea. Since the United States has a very laissex-faire economic policy, we suppose their governmental military expenditures will present opportunity costs which impari future spending. Therefore we assign $b$ as 0.5 $year^{-1}$ for South Korea and $c$ 0.8 $year^{-1}$ for the United States.
# 
# Finally, we assume all the countries have similar levels of fear of or sentiments of animosity towards other countries. However, since North Korea faces two allies, we assume their fear could be closer to twice that of the other countries. Therefore we assign $g$ as 5000 and $h$ and $i$ as 3000, all with units of $\frac{USD \; in \; millions}{year}$.
# 
# With all these parameters, the model assumes the folowing form:
# 
# $$\frac{dx}{dt} = -1.0x+0.35y+0.35z+5000$$
# 
# $$\frac{dy}{dt} = −0.5y+0.38x+0.35z+3000$$
# 
# $$\frac{dz}{dt} = −0.8z+0.38x+0.35y+3000$$

# ### First Model Extension Analysis

# We again study the long-term behaviours of the model to understand the dynamics between the three countries military expenditures. This allows for the determination of how their spending changes over time, such as whether their expenditures will increase unbounded or be bounded by some upper limit. We simulate the annual military expenditures of each of the three countries and plot them against time and perform a mathematical analysis to determine the existance of any equilibrium. We also investigate the stability of these equilibrium to determine how the spending of each nation changes near any equilibrium such as if their spending is fluctuating or approaching on a straight trajectory.
# 
# To show whether an equilibrium for the extended Richardson Model of Armaments Races exist under the variations of paramters chosen above, we look for the existence of fixed points by determining where the change in spending of both countries is equal to zero ($\frac{dx}{dt}=\frac{dy}{dt}=\frac{dz}{dt}=0$). Since we assume all the parameters are greater than zero, it can be shown that the sole fixed point of all the model exists at:
# 
# $$x_0 = \frac{-(bcg + bim + chl + ilm - glm + hlm)}{(alm - abc + bkm + ckl + 2klm)} $$
# 
# $$y_0 = \frac{-(ach + aim + cgk + ikm + gkm - hkm)}{(alm - abc + bkm + ckl + 2klm)}$$
# 
# $$z_0 = \frac{-(abi + bgk + ahl - ikl + gkl + hkl)}{(alm - abc + bkm + ckl + 2klm)}$$
# 
# Under the parameters described above for this model, the fixed points exist at:
# $$
# \begin{align}
# x_0 &= 65540.54054054046\\
# y_0 &= 104054.05405405392\\
# z_0 &= 80405.4054054053\\
# \end{align}
# $$
# 
# Subsequently we determine the nature of the stability, if it is indeed stable, at this fixed point. We examine the trace-determinant plane to show if each countries spending will approach some value correpsonding to each of their spending, or move away from it. We first find the Jacobian matirx J, which is shown below. The equilibrium fixed point will be stable if the trace of the Jacobian is less than zero and the determinant of the Jacobian is greater than zero.
# $$J = \begin{bmatrix} -a & l & m  \\ -b & k & m \\ -c & k & l \end{bmatrix}$$
# 
# $$tr(J) = k + l - a $$ 
# 
# $$det(J) = a k (m - l) + b (l^2 - k m) + c m (k - l)$$
# 
# Therefore, we find that the equilibrium fixed point is stable when the following conditions are satisfied:
# 
# $$
# \begin{align}
# k+l &< a\\
# (akm+bl^2+cmk) &> (akl + bkm + cml)
# \end{align}
# $$
# 
# Given our chosen parameters, we find that the equilibrium does comply with the required conditions, thus making it stable. This means that the model will not increase unbounded, but instead will gradually tend towards some value which is above the current military expenditures for each respective country.
# 
# Finally, we determine the nature of the stability to see how the trajectory of the model moves in order to analyze how the expenditure for each country fluctuates as they all stabilize in the long-term. 
# 
# Given our conditions for stability, we can see that the trace is negative and the determinant is positive, which shows we have some type of sink. If we check the equations for the eigenvalues, we can see that:
# 
# $$ \lambda_{1,2} = \frac{tr(J) \pm \sqrt{tr(J)^{2} - 4det(J)}}{2} $$
# 
# With our given parameters, the expression $$tr(J)^{2} - 4det(J)$$ is evaluated to be a number greater than zero, which indicates that the eigenvalues are real and thus the equilibrium is a nodal sink. This implies that over time, we expect the military expenditure of all countries to degenerate to the fixed point and stabilize there. Since the equilibrium of the model suggests the military expenditures will tend towards the values of the fixed point over time, the fixed point in our given simulation indicates that South Korea will end up with the highest annual military expenitures, North Korea with the lowest and the United States with an intermediate annual military expenditure.
# 
# The numerical simulation of the parameters which give this equilibrium in the extended Richardson model described above is plotted below.

# In[ ]:


# Numerical simulation of extended Richardson Model (Three Countries)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(s,t):
    a = 1
    b = 0.5
    c = 0.8
    k = 0.38
    l = 0.35
    m = 0.3
    g = 5000
    h = 3000
    i = 3000
    x = s[0]
    y = s[1]
    z = s[2]
    dxdt = -a * x + l * y + m * z + g
    dydt = -b * y + k * x + m * z + h
    dzdt = -c * z + k * x + l * y + i
    return [dxdt, dydt, dzdt]

t = np.linspace(0,50,600)
s0=[1600, 47000, 785000]

s = odeint(f,s0,t)

plt.plot(t,s[:,0],'r', linewidth=2.0, label = "North Korea")
plt.plot(t,s[:,1],'k', linewidth=2.0, label = "South Korea")
plt.plot(t,s[:,2],'b', label = "United States")
plt.xlabel("t (years)")
plt.ylabel("Annual Military Expenditures (million USD)")
plt.legend()
plt.title("Extended Three Country Model of Armament Expenditures")
plt.show()


# ### Second Model Extension

# Despite the arms race being between North and South Korea, the effect that they have on each other is not the only thing that can increase or decrease their armament spending. In this extension, we introduce the concept of submissiveness, where fear of other nations can help limit the arms expenditure of both countries. As an arms race between two countries will no doubt leave the rest of the world suspicious, disapproving, or on edge, both North and South Korea will need to limit their expenditure at one point in order to not create unrest between them and the rest of the world. In order to avoid international backlash, and possibly sanctions against them, North and South Korea will occasionally reduce their spending depending on how other countries react to their arms race. 
# 
# &nbsp;
# 
# This can be modelled by the following equations,
# 
# $$
# \begin{align}
# \frac{dx}{dt} &= ay(1 - f(y - x)) - mx + r \\
# \frac{dy}{dt} &= bx(1 - g(x - y)) - ny + r
# \end{align}
# $$
# 
# Where $x$ and $y$ represent the expenditure in millions of USD of North and South Korea respectively, and $t$ is time in years, thus $t>0$. $a$ and $b$ are the reaction coefficients, and thus represent the proportion that each country will spend on armaments in relation with the other country's expenditure. $m$ and $n$ represent the coefficient of fatigue, as the governments can only spend so much on the military before it puts a strain on the economy. $f$ and $g$ are the coefficients of submissiveness caused by potential political backlash, therefore as the coefficients get larger, so will the reduction in arms. $r$ and $s$ represent the amount of grievance and goodwill the countries have toward each other. 
# 
# Where $a, b, f, g, m, n, r, s > 0$. This model assumes that $r$ and $s$ are both positive, as North and South Korea have hostile relations, thus they would only have feelings of grievance. $f$ and $g$ are also assumed to be positive and small numbers, as we will be assuming that international innfluence will only reduce arms spending of the country, as well as that influence having a small effect. 
# 
# &nbsp;
# 
# In our given simulation, we outline a scenario where North Korea is spending a larger amount of money proportional to South Korea, which can be seen through the parameters $a = 0.5$ and $b = 0.28$. We also see that $m = 0.38$ and $n = 0.35$, which implies that the strain on their economy is relatively equal. We have $r = 50$ and $s= 30$, showing that they both have grievances towards each other, with North Korea's being slightly higher. Given this information, in this simulation North Korea is being portrayed as the aggressor that pushes the arms race further. 
# 
# There are three cases to consider when looking at the effect of the coefficient of submission. The first case is when $f$ and $g$ are roughly equal. We can see in Project Model 1 that both North and South Korea have roughly the same submission values, $f = 0.004$ and $g = 0.003$, where North Korea's is only slightly higher. From the trajectory, we can see the behaviour of a spiral sink. Thus, as time goes on, in the long-term the armament spending of both countries will stabilize at some equilibrium which is the center of the spiral sink. 
# 
# The second case to consider is when North Korea has a lower coefficient of submission than South Korea given the same scenario. In this case, we have $f = 0.001$ and $g = 0.003$. As we can see from Project Model 2, the trajectory still displays the behaviour of a spiral sink. However, we can see that the expenditure point that each country will stabilize to in the long-run, has increased for both North and South Korea. This can be explained as the result of North Korea having less fear, thus being able to spend more on their armaments. In return, due to North Korea's increased spending, South Korea will then react and also have their expenditure increase in turn. 
# 
# The third case to consider is when North Korea has a higher coefficient of submission compared to South Korea, with the rest of the parameters staying the same. In this case, we have $f = 0.004$ and $g = 0.001$. The trajectory of the model once again displays the behaviour of a spiral sink. This means, that over time, the expenditure will circle around the fixed point, getting closer as time goes on, until it eventually stabilizes in the long-run at that fixed point. We can see in Project Model 3 that despite South Korea having the smaller submission coefficient, it is actually North Korea's spending that increases. While one may assume that due to the heavier limits being put on North Korea that North Korea's spending would shrink, it is actually the opposite. It can be interpreted that because South Korea is able to spend more without as many limitations, North Korea in turn is obligated to increase their own spending by a higher proportion in order to compensate. Thus, the smaller submission coefficient for South Korea, paired with North Korea being the aggressive country, results in an increased spending for both, but North Korea especially.
# 
# This can be further analyzed by looking at the expanded equation.
# 
# $$
# \begin{align}
# \frac{dx}{dt} &= ay - afy^2 + afyx - mx + r \\
# \frac{dy}{dt} &= bx - bgx^2 + bgxy - ny + r
# \end{align}
# $$
# 
# Taking a closer look at the equation for North Korea, specifically the terms containing $f$ which is the coefficient of submission, we can see in $-afy^2$ that a proportion of what was initially spent due to South Korea's spending is deducted due to the submission factor. However, in the term $+afyx$ we can see the interaction of the submission coefficient with the reaction coefficient $a$, and the spendings of both North and South Korea, $x$ and $y$ respectively. Thus looking at our model parameters for Project Model 3, we can see that as the coefficient of submission decreases for South Korea, $y$ will increase, thus leading to a higher spending from North Korea despite its own limitations.
# 
# Overall, looking at the trajectory of all our models, we can see that despite what the coefficient of submission may be, the models depict a spiral sink, thus in the long-term, the military expenditure of each country will be attracted to that fixed point until it eventually reaches that center and stabilizes there. This means that over time, as the spending of each country fluctuates, they will both gravitate towards some value where it will stay at. However, this is not to say that there is no effect from the coefficient of submission. As we can see from our simulation, it can greatly cause an impact on both countries' expenditure.

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import integrate

def df_time_delay_arm_race(mod, params, t, X0):
    X = integrate.odeint(mod, X0, t, args=params)
    f = plt.figure()
    plt.plot(X[:,0], X[:,1])
    
    
    xmax = plt.xlim(xmin=0)[1]
    ymax = plt.ylim(ymin=0)[1]
    
    n_points = 20
    
    x = np.linspace(0, xmax, n_points)
    y = np.linspace(0, ymax, n_points)
    
    X1, Y1 = np.meshgrid(x, y)
    DX1, DY1 = mod([X1, Y1], 0, params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7])
    
    M = (np.hypot(DX1, DY1))
    M[M == 0] = 1.
    
    DX1 /= M
    DY1 /= M
    
    plt.title('ARMS RACE')
    Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.plasma)
    plt.xlabel('North')
    plt.ylabel('South')
    plt.grid()
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.show

def time_delay_arm_race(X, t, a, b, f, g, m, n, r, s):
    x, y = X[0], X[1]
    return [a*y - a*f*y*y + a*f*y*x- m*x + r, b*x -b*g*x*x + b*g*y*x -n*y + s]

params1 = (0.5,0.28,0.004,0.003,.38,0.35,50,30)
params2 = (0.5,0.28,0.001,0.003,0.38,0.35,50,30)
params3 = (0.5,0.28,0.004,0.001,0.38,0.35,50,30)
X0 = [160, 470]
t = np.linspace(0, 100, 1000)

df_time_delay_arm_race(time_delay_arm_race, params1, t, X0)
plt.title('Project Model 1')
df_time_delay_arm_race(time_delay_arm_race, params2, t, X0)
plt.title('Project Model 2')
df_time_delay_arm_race(time_delay_arm_race, params3, t, X0)
plt.title('Project Model 3')


# # Stochastic Element

# The base model we have employed, the Richardson Model of Armament Races, does not consider any stochasticity. It assumes that greivances between antagonistic nations is a constant, however this is not applicable to real life as there are factors that influence greivances the Richardson Model omits.
# 
# One of the Richardson models limitations is that it makes decisions deterministically and does not consider the variations or fluctuations in opinions and political agendas of defense planners from within either nation. To combat this shortcoming,  we introduce the stochastic differential equation (SDE; Caspary, W.R., 1967), which was originally a field of mathematics whose purpose was to study brownian motion - a phenomena that describes the random motion of particles in a suspended medium of fluid. SDEs are classic differntial equations which are perturbed by some random noise. An SDE can represent an ordinary differential equation (ODE) given no noise parameters. The implementation of SDE's into our model, now allows us to observe random fluctuations in armament expenditure such as the sometimes abrupt decisions carried out by political figureheads.
# 
# Fundementally, an SDE is a function whose coefficients are random functions of independent variables. For the purpose of our arms race modelling, we will be using the Ornstein-Uhlenbeck (O-U) SDE given by $dX_{t} = κ(θ-X_{t}) dt + σdW_{t}$, 
# where we set r = s = $dX_{t}$ in our initial model. κ represents the mean reversion (medium.com, "stochastic-differential-equations-the-ornstein-uhlenbeck-process"), or the assumption that grievance converges to an averaged value; θ is the long term mean and sigma is the volatility, or standard deviation of the brownian motion (medium.com "stochastic-differential-equations-the-ornstein-uhlenbeck-process").
# 
# The simulation above depicts the implementation off O-U stochasitcity in the original pair of differential equations. Using a mean of 100 and a standard deviation of 0.1, we are able to duplicate the non-stochastic simulation of the base model.
# 

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import random as rd

def df_stochasticity(mod, params, t, X0, mu):
    """
    Function plotting base model of arms race on two-dimensional vector field.
    """
    
    X = integrate.odeint(mod, X0, t, args=params)
    f = plt.figure()
    plt.plot(X[:,0], X[:,1])
    plt.plot((params[4]*params[2]+params[0]*params[5])/(params[1]*params[4]-params[0]*params[3]),
            (params[3]*params[2]+params[1]*params[5])/(params[1]*params[4]-params[0]*params[3]),'ro')
    
    xmax = plt.xlim(xmin=0)[1]
    ymax = plt.ylim(ymin=0)[1]
    
    n_points = 20
    
    x = np.linspace(0, xmax, n_points)
    y = np.linspace(0, ymax, n_points)
    
    X1, Y1 = np.meshgrid(x, y)
    DX1, DY1 = mod([X1, Y1], 0, params[0], params[1], params[2], params[3], params[4], params[5])
    
    M = (np.hypot(DX1, DY1))
    M[M == 0] = 1.
    
    DX1 /= M
    DY1 /= M
    
    plt.title(f'Stochasticty for a mu of: {mu}')
    Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.plasma)
    plt.xlabel('North Korea Armament Expenditure (million USD/year)')
    plt.ylabel('South Korea Armament Expenditure (million USD/year)')
    plt.grid()
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.show()

def base_model(X, t, a, m, r, b, n, s):
    x, y = X[0], X[1]
    return [a*y - m*x + r, b*x - n*y + s]


# In[ ]:


mu = 100
sigma = 0.1  

params = (0.5,0.38,rd.normal(mu, sigma),0.25,0.35,3000) 
X0 = [1600, 47000]
t = np.linspace(0, 1000, 1000)


df_stochasticity(base_model, params, t, X0, mu)


# If we adjust the mean to 1000 and keep the standard deviation constant we get:

# In[ ]:


mu = 1000
sigma = 0.1

params = (0.5,0.38,rd.normal(mu, sigma),0.25,0.35,3000) 
X0 = [1600, 47000]
t = np.linspace(0, 1000, 1000)


df_stochasticity(base_model, params, t, X0, mu)


# The stochastic plots of the two graphs are very similar. A change of mu of a scale of 10 seems to not effect the overall model. Next we will be looking at differernt values of μ at a constant σ = 0.1 to see if there are any notable changes in 0 < μ < 10000.

# In[ ]:


X0 = [1600, 47000]
t = np.linspace(0, 1000, 1000)
mu = 0
sigma = 0.1
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 1000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 2000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 3000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 4000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 5000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 6000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 7000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 8000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 9000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)
mu = 10000
params = (0.5,0.38,rd.normal(mu,sigma),0.25,0.35,3000) 
df_stochasticity(base_model, params, t, X0, mu)


# The simulation for different stochasticity's returns similar curves for different values of μ. At a point around (40000,35000) on each graph the arms acquisition turns linear similar to our base model. This infers that stochastic elements have little to no effect on how two nations purchase arms. 

# # Discussion and Conclusion

# 
# 
# In conclusion, there are many factors that can either increase or decrease further spending for both North and South Korea in an arms race. This can be clearly shown through our analyses of our base model, its extensions, and our stochastic element. Overall, we can see that in each of our numericallly simulated models, the armaments expenditure for each country in the long run will eventually stabilize at some equilibrium fixed point. The involvement of a third country, the influence of outside factors, and the inclusion of a stochastic element have all shown to have an effect on the amount of spending each country completes, yet overall in the long-term, it does not change the fact that the nations will stabilize their spending at some fixed point instead of having an unbounded arms race. 
# 
# In further studies on this topic, a helpful concept to add to the model would be an economic constraint. One of the limitations of this model is that it does not take into account the fact that each government can only spend so much on their military each year. While there is a term that does consider the economic strain that an arms race has on the country, it does not cap or limit the expenditure the way a carrying capacity would. Further influences that would be interesting to study in an arms race are how the technological advancement of each country may affect their spending. A country that is more technologically advanced may have a greater spending than one that is less advanced. 
# 
# Another concept to consider would be the effect of alliances and whether it will deter or invigorate their spending. In our third country model, North Korea, South Korea, and the USA were all assumed to have a mutual level of hostility; thus, their armament expenditure was all proportional. However, in the real world that is not the case, as North Korea has a more hostile relationship with the USA and South Korea, while the latter two do not have such a tense relationship. Thus, the spending of North Korea should alarm South Korea and the USA more than South Korea and the USA should alarm each other, which is not depicted in our model. Taking this into account would be an interesting area of further study, especially if you consider an arms race between two countries where one is disadvantaged in its military strength and arms spending yet has powerful allies that will deter any threats.
# 
# 

# # Code

# *See code embedded throughout the document.*

# In[ ]:





# # References

# Azam, M. (2020). Does military spending stifle economic growth? The empirical evidence from non-OECD countries. Heliyon, 6(12). https://doi.org/10.1016/J.HELIYON.2020.E05853
# 
# Bhattacharjee, M., & Mazumdar, D. (1 C.E.). The Opportunity Costs of Military Expenditure. Https://Services.Igi-Global.Com/Resolvedoi/Resolve.Aspx?Doi=10.4018/978-1-5225-4778-5.Ch015, 271–284. https://doi.org/10.4018/978-1-5225-4778-5.CH015
# 
# Caspary, W. R. (1967). Richardson’s Model of Arms Races: Description, Critique, and an Alternative Model. International Studies Quarterly, 11(1), 63–88. https://doi.org/10.2307/3013990
# 
# Howe, R. (2021, July 18). Stochastic differential equations -the Ornstein-Uhlenbeck process. Medium. Retrieved April 21, 2022, from https://medium.com/star-gazers/stochastic-differential-equations-the-ornstein-uhlenbeck-process-17bca1c1ef37 
# 
# Intriligator, M. D. (2015). Strategic Considerations in the Richardson Model of Arms Races. Https://Doi.Org/10.1086/260326, 83(2), 339–354. https://doi.org/10.1086/260326
# 
# Military Expenditures – UNODA. (n.d.). Retrieved April 18, 2022, from https://www.un.org/disarmament/convarms/milex/
# 
# Negative views of Russia on the Rise: Global Poll. (2014).
# 
# RICHARDSON, L. Could an Arms-Race End Without Fighting?. Nature 168, 567–568 (1951). https://doi.org/10.1038/168567b0
# 
# SIPRI Military Expenditure Database | SIPRI. (n.d.). Retrieved April 18, 2022, from https://www.sipri.org/databases/milex
# 
# Smoker, P. (1964). Fear in the Arms Race: A Mathematical Study. Journal of Peace Research, 1(1), 55–64. https://doi.org/10.1177/002234336400100105åç
# 
# United States. Defense Intelligence Agency. (n.d.). North Korea military power : a growing regional and global threat.
# 
# van der Meer, S. (2011). Geopolitics and nuclear weapons. North Korean provocations as a tool for regime survival. Studia Diplomatica, 64, 53–65.
#  
# Wallace, M. D. (1979). Arms Races and Escalation: Some New Evidence. The Journal of Conflict Resolution, 23(1), 3–16. http://www.jstor.org/stable/173649
# 
# 
# 
# 
# 

# In[ ]:




