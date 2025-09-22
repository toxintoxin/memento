+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "BP-pacFA-protocol"
+++

ref:  
[Trifunctional Sphinganine: A New Tool to Dissect Sphingolipid Function](https://doi.org/10.1021/acschembio.3c00554)  
[In Vivo Profiling and Visualization of Cellular Protein–Lipid Interactions Using Bifunctional Fatty Acids](https://doi.org/10.1002/anie.201210178)

copper sulfate, 探索  
TCEP(Tris(2-carboxyethyl)phosphine hydrochloride), SIGMA, C4706, (L-Ascorbic acid, SIGMA, A92902)  
TBTA(Tris[(1-benzyl-1H-1,2,3-triazol-4-yl)methyl]amine), SIGMA, 678937  
Azide-fluor 488, SIGMA, 760765  

preparation:  
500mM copper sulfate stock: 7.98g溶解到80ml去离子水中, 定容到100ml, 常温保存  
100mM TBTA stock: 1 mg + 18.8 μl DMSO, stored at -20  
2mM azide-A488 stock:  1 mg + 870 μl DMSO, stored at -20  

click mix:  
1mM copper sulfate  
1mM TCEP (or 1mM sodium ascorbate)  
100μM TBTA  
2μM A488-azide (or 2μM others)  
in PBS  

当天配置50mM的抗坏血酸, 每10mg加1130μlPBS, 取所需量的体积用PBS稀释到1mM, 再加入其他试剂

1. 100μM OA诱导脂滴，具体时间视细胞系决定，Hela细胞24h，Huh7细胞3h(为了成像，结束诱导时具有60%左右的confluence，据此处把握一开始seeding的细胞量)
2. wash twice with HBSS
3. incubate with 10μM BP-pacFA in HBSS for 10min at 37°C
4. expose to 525nm light for 2min to uncage the probe
5. return to the incubator for varying amounts of time to allow for metabolism
6. expose to 365nm light for 5s to cross-link on ice, and immediately replaced with ice-cold methanol (-20°C) for 20min on ice
7. wash three times with CHCl3/MeOH/AcOH (10:55:0.75, v/v/v) for 1min each time at RT
8. wash three times with PBS for 5min each time
9. add click mix (400μl for 24-well plates, 70μl for 96-well plates)
10. incubated for 1 h in the dark on a shaker
11. wash twice with PBS to remove the click mix

**Antibody staining**

1. blocking buffer (2% BSA, 0.1% Triton-X-100 in PBS) was added. Cells were blocked for 1 h before the addition of primary antibodies
2. incubate with primary antibody
