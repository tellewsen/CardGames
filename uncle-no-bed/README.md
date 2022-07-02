# uncle-no-bed
Card game test to see how often we should expect to win

Running with n=100.000 we finish in 37m55s
<table>
<tr><td> </td><td>ms</td><td>ss</td><td>sf</td><td>mr</td><td>mp</td></tr>
<tr><td>Won</td><td>63</td><td>48</td><td>40</td><td>59</td><td>98</td></tr>
<tr><td>Pct</td><td>0.063</td><td>0.048</td><td>0.04</td><td>0.059</td><td>0.098</td></tr>
</table>

<b>ms</b> is the strategy where we do ten tries of random choices when we have to pick, and pick the one with the least stacks left.

<b>ss</b> is the strategy where we the one where we always chooce to take the one step move when we have to choose.

<b>sf</b> is the one where we always choose the long move when we can choose.

<b>mr</b> it he one where we just pick at random when we have to choose.

<b>mp</b> is the one where we try to walk all the paths, and then pick the one with least stacks on the table

This can definitely be optimized by quite a bit. I'll see if I bother at some point.