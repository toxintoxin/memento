+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "siRNA transfection"
+++

## 试剂

- siRNA（公司一般会提供3种siRNA，1个通用阴性对照，1个FAM标记通用阴性对照，1个GAPDH阳性对照）
- 转染试剂为Lipo2000或Lipo3000
- Opti-MEM，或者简单化为无抗生素无血清培养基（特殊的，若转染BMDM的话，需补充20ng/mL的M-CSF）

## 环境

- siRNA长期放置最好以冻干粉形式保存，可保存1年以上。第一次溶解时先勿开盖，在1000g，4°C离心1min后，用DEPC水溶解至20pmol/μL（推荐值），分装保存，避免反复冻融，-20°C至-80°C可保存半年以上。
- siRNA最好冰上放置，整个实验过程，要求RNA酶free，枪头、EP管等都应该经过无酶处理。

## 转染前准备

- 至少3个平行重复
- 推荐转染使用的细胞密度为70%-80%
- 建议转染前12h更换细胞培养基为Opti-MEM

## 转染步骤

以下步骤以24孔板为例，所有用量和体积均按每孔给出。对于其他规格，请参见[“扩大或缩小转染规模”](#扩大或缩小转染规模)。

1. 稀释siRNA：在无菌管中加入50μL的Opti-MEM，再加入20pmol的siRNA低聚体，用移液枪轻轻混匀，室温静置5min。
2. 稀释转染试剂：在另一无菌管中加入50μL的Opti-MEM，再加入1μL的Lipo2000，用移液枪轻轻混匀，室温静置5min。
3. 将已稀释的Lipo2000加入到已稀释的siRNA低聚体中，用移液枪轻轻混匀，室温静置15min。（不能静置超过30min，最好15min后立即加入孔板）
4. 将siRNA低聚体-Lipo2000复合物添加至孔板中，轻轻晃动细胞板至均匀分布。
5. 根据后续实验需求在培养箱中孵育细胞24-96小时。24-48h检测mRNA表达（qRT-PCR），48-96h检测蛋白表达（Western Blot）。
6. 可在6-8h更换为完全培养基，避免细胞长时间饥饿造成的细胞活力损失。

### 扩大或缩小转染规模

| Culture vessel | Surf. area per well<sup>1</sup> | Vol. of plating medium | Vol. of dilution medium<sup>2</sup> | RNA      | Lipofectamine 2000 |
| -------------- | ------------------------------- | ---------------------- | ----------------------------------- | -------- | ------------------ |
| 96-well        | 0.3 cm <sup>2</sup>             | 100 µl                 | 2 x 25 µl                           | 5 pmol   | 0.25 µl            |
| 24-well        | 2 cm <sup>2</sup>               | 500 µl                 | 2 x 50 µl                           | 20 pmol  | 1.0 µl             |
| 12-well        | 4 cm <sup>2</sup>               | 1 ml                   | 2 x 100 µl                          | 40 pmol  | 2.0 µl             |
| 6-well         | 10 cm <sup>2</sup>              | 2 ml                   | 2 x 250 µl                          | 100 pmol | 5 µl               |
| 60-mm          | 20 cm <sup>2</sup>              | 5 ml                   | 2 x 0.5 ml                          | 200 pmol | 10 µl              |
| 10-cm          | 60 cm <sup>2</sup>              | 15 ml                  | 2 x 1.5 ml                          | 600 pmol | 30 µl              |

<sup>1</sup> Surface areas may vary depending on the manufacturer.  
<sup>2</sup> Volumes of dilution medium in Step 2a & 2b of DNA or RNAi transfection protocols.  

## Reference

1. [Lipofectamine 2000](https://www.thermofisher.com/us/en/home/references/protocols/cell-culture/transfection-protocol/lipofectamine-2000.html)
2. [Guidelines for RNA Transfection](https://www.thermofisher.com/us/en/home/references/gibco-cell-culture-basics/transfection-basics/guidelines-for-rna-transfection.html)
3. [Optimizing siRNA Transfection](https://www.thermofisher.com/us/en/home/references/gibco-cell-culture-basics/transfection-basics/guidelines-for-rna-transfection/optimizing-sirna-transfection.html)
4. [Selecting an RNAi Strategy](https://www.thermofisher.com/us/en/home/references/gibco-cell-culture-basics/transfection-basics/guidelines-for-rna-transfection/selecting-an-rnai-strategy.html)