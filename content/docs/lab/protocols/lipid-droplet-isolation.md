+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "Lipid droplet isolation"
+++

ref: https://doi.org/10.1038/nprot.2012.142

> 7h提取15-100μg蛋白当量的高质量脂滴

> 声称是第一篇详细的protocol，提取脂滴已经有30多年的历史了

> 由于该方案包含用于超速离心后的LDs的几个洗涤步骤，在某些情况下，在超速离心法和洗涤步骤期间都可能丢失非常小的LDs。此外，超大尺寸的LDs在匀浆和超速离心过程中可能会被破坏。在真核生物中，与LDs物理接触的少量膜结构可能与LDs共分离，如果目的是关注LD相关蛋白，这是不可取的。

> briefly, washed and homogenized in 250mM sucrose to protect intracelluar organelles, then ultracentrifuged to separate LDs, collected and washed.

## MATERIALS

| Name                   | Brand, Cat. No.          |
| ---------------------- | ------------------------ |
| PBS                    | 碧云天, ST447-5L         |
| Sucrose                |                          |
| Tricine                | Sigma-Aldrich, T0377-25G |
| KOH                    |                          |
| HEPES                  |
| KCl                    |                          |
| MgCl<sub>2</sub>       |                          |
| PMSF                   | Sigma-Aldrich, P7626-1G  |
| DMSO                   |
| SDS                    |
| 研钵                   |
| gel-loading tip(200μl) |

## REAGENT SETUP

> **PBS** 灭菌后保存于4°C

> **Sucrose (2.5 M, 600ml)**  
> 称取500g sucrose，加入300ml去离子水，磁力搅拌至完全溶解。保存于4°C。  
> 3个月  
> 需要很长时间溶解，需要提前配置。  

> **Buffer A (500ml, 20mM tricine, 250mM sucrose (pH 7.8))**  
> 400ml去离子水，加入1.79g tricine，用100mM KOH调节PH到7.8。加入50ml sucrose母液 (2.5M)，补足至500ml。灭菌后保存于4°C。  
> 3个月  

> **Buffer B (200ml, 20mM HEPES, 100mM KCl, 2mM MgCl<sub>2</sub> (pH 7.4))**  
> 180ml去离子水，加入0.95g HEPES，1.49g KCl，0.038g MgCl<sub>2</sub>，用100mM KOH调节PH到7.4，补足至200ml。灭菌后保存于4°C。  
> 3个月  

> **PMSF (10ml, 1000×, 0.2M)**  
> 称取0.35g PMSF，用10ml DMSO溶解，分装成1ml，避光保存于-20°C。  
> 1年  
> PMSF有毒  

> **SDS** 买预制  

## PROCEDURE

### 从组织开始

> 必须使用新鲜的组织，不可以冷冻  
> 取样根据脂肪含量不同而大小不同，如果是肝脏需要两片肝  

1. 在研钵中加入冷的Buffer A(含0.2mM PMSF)12mL
2. 加液氮使用研钵研磨后（约10 次），500 xg, 4°C, 离心5min，吸出上层溶液放冰上待用。

### 从组织匀浆液或cell culture开始

1. 6个150mm dish为一个样本, 胰酶消化并离心后, 用9 mL Buffer A with 0.2 mM PMSF重悬合并
2. 破碎细胞：在冰上使用35bar 15min 破碎细胞。(细胞破碎仪的话, 经验来说, 800bar破碎4遍)
3. 1,000 xg, 4 °C, 离心10min, 去除细胞核及细胞碎片。保留上层溶液 (PNS)，分装200μL在冰上用于最后LD 纯度检测。
4. 转移PNS到SW41 tube中，并在上层加入2mL BufferB（可以多加一点，加的越多LD 越纯）
5. 离心：肝脏为2,000 xg，30min；细胞为40,000 rpm，3h
6. 用枪头小心收集最上层的LD，尽可能多的吸取LD，应为纯白色，可分装一部分用于计算total fraction的比值。（枪头吸之前先用Buffer B润一下，一次吸少于10μL，少量多次）
7. 吸取1ml离心后的胞质，270000g离心1h，收集上层并分装500μL作为Cytosol fraction
8. 吸出中间层，并在SW tube沉淀中加入1mL Buffer B重悬，吸取50μL作为total membrane fraction
9. 将脂滴离心17,000 xg, 10min, 用gel-loading tip吸出上层溶液。每管LD不超过10μL，若超过需要分装。(实际情况弃去下层溶液保留上层白色脂滴更为简单)
10. 用200μL Buffer B重悬后重复上一步骤。洗两次。

> 最后获得的脂滴, 可以加入1 mL CHCl3/Acetone (1/1, v/v), vortex, 17,000 xg, 4 °C, 离心10 min, 上清用于提取脂质, 沉淀用PBS溶解用于WB

### LD质量评估

#### LipidTox染色

#### 通过WB和数据分析评估LDs质量

An important way to check the purity of LDs obtained is to perform western blotting to determine the distribution of marker proteins between the LD fraction and other cellular fractions. With regard to the normalization of data in western blotting, we think that it is better to present the data with respect to the amount of protein used rather than as a percentage of the amount of starting material used, as it is unclear how many LDs are lost during the purification process. Therefore, we recommend using equal protein loading to determine the enrichment of marker proteins to judge the purity of LDs. However, as a parallel analysis, it is useful to sample and compare fractions after collection of LDs and before the washes by loading an equal percentage of the total fractions.
<!-- 
| Sample                 | Starting amounts                                   | Sample collection (Step 1)                                                                                                                                                      | Homogenization (Steps 3 and 4)                                                                                                                                                         | Ultracentrifugation (Step 8)                                          | Typical yield of LD protein (μg) | Typical size range of LDs (μm) |
| ---------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------- | ------------------------------ |
| Caenorhabditis elegans | 4 × 10^5^ worms                                    | Wash the worms three times with 50 ml of PBS plus 0.001% (vol/vol) Triton X-100 and then once with 50 ml of buffer A. Resuspend the worms in 10 ml of buffer A with 0.2 mM PMSF | Homogenize the worms four times on ice with a Polytron at 14,000 r.p.m., 1 min per time with 30-s intervals. Centrifuge at 1,000g for 30 s, keep the supernatant and proceed to Step 5 | 10,200–10,600g for 1 h at 4 °C                                        | ~30                              | 0.5–2                          |
| Mouse skeletal muscle  | Muscle dissected from hind legs of 20 C57BL/6 mice | Remove the fascia and connective tissues, then cut into small pieces and resuspend in 12 ml of buffer A with 0.2 mM PMSF                                                        | Homogenize on ice 20 times with a tight-fitting Dounce. Centrifuge at 100g for 10 min at 4 °C, keep the supernatant and proceed to Step 5                                              | 182,000g for 1 h at 4 °C                                              | ~15                              | 0.5–1                          |
| Mouse liver            | Livers of two C57BL/6 mice                         | Remove the fascia and connective tissues, then cut into small pieces and resuspend in 12 ml of buffer A with 0.2 mM PMSF                                                        | Homogenize on ice ten times with a loose-fitting Dounce. Centrifuge at 100g for 10 min at 4 °C, keep the supernatant and proceed to Step 5                                             | 2,000g for 30 min at 4 °C                                             | ~100                             | 1–5                            |
| CHO-K2 cells           | Cells from ten 150-mm plates (100% confluent)      | Wash the dishes with 10 ml of icecold PBS. Scrape the cells and resuspend in 100 ml of PBS, and centrifuge at 1,000g for 10 min at 4 °C to collect cells                        | None required.<br>Proceed directly to Step 5                                                                                                                                           | 182,000g for 1 h at 4 °C                                              | ~20                              | 0.1–1                          |
| Bacteria/yeast         | 400 ml of liquid culture in stationary phase       | Collect the cells by centrifuging the culture at 4,000g for 10 min. Wash the cells twice with 30 ml of PBS and collect cells                                                    | None required.<br>Proceed directly to Step 5                                                                                                                                           | 10,200–10,600g for 1 h at 4 °C for yeast and 182,000g for 1 h at 4 °C | ~25                              | 0.1–1                          |

 -->
