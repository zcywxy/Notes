[[ReadItLater]] [[Article]]

# [墙裂推荐！万字长文掘地三尺找出你的基因A。](https://mp.weixin.qq.com/s/COaKjsezlL90eqZ56l1bjQ)

#### 果子荐读：

首先我们推出了一个[人人都该掌握的批量技能](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650735312&idx=1&sn=f5112522e84e6ca17fb79cf5fbf5da22&scene=21#wechat_redirect)。  
接着我们邀请了[一些朋友分享了学习笔记](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650735335&idx=1&sn=8e4dc669b0c420ba51446fc30b41e395&scene=21#wechat_redirect)  
今天是晓杰的分享，晓杰上一次的分享，准备了大概150个小时，写了一篇无论什么时候读都不过时的帖子。  
[墙裂推荐！统计方法如何选以及全代码作图实现。](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650734365&idx=1&sn=f18633e789ad18efd3c82fe156e60af6&scene=21#wechat_redirect)  
优秀的人，再小的事情都会认真对待。  
这次他用批量技能，复现了一篇《Advanced science》的多个图表，全程高能，是个很好的学习技能的例子。  
这让我想起来了5年前写过的一个帖子，展示如何拿到一个基因A后设计并开展实验，这个帖子目前有1万4000人阅读，很多人留言表示感谢。  
[课题设计：收不完的病人查不完的房，临床医生如何快速地设计一个靠谱的课题？](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650732330&idx=1&sn=35751c91d8cbd62cf988679701f9da8e&scene=21#wechat_redirect)  
在这个帖子的最后我挖了一个坑，留下了一个困扰我很多年的题目：  

当时我自信满满，以为很快就能写出，但是最终发现能力不够，花了5年才有点眉目。  

如果硬着头皮厚着脸皮的去分享，估计得看千百篇文献，写好几个帖子，而我一直难以动笔，不过我看了晓杰的分享，觉得可以作为开篇，大家可以学习里面的技术，

> 学习新技能不会立马改变世界，但他就像一副眼镜，戴上他，世界没有变，你看得更清楚了。

推荐给大家。

以下是正文：

---

时隔一年，再次接到果子老师的邀稿，内心是激动与澎湃的；一年前写稿子的情景，还历历在目，笔记记载的是自己的成长和回忆，很高兴帮助到了很多朋友：

为了写这个稿子，我想了很久，应该从哪个角度入手，觉得还是最好从运用的角度来写，会好一些，下面将从文献实例来写。

---

### 一、灵感来源

首先是《Advanced science》上2020年一篇文章：，[Direct Targeting of CREB1 with Imperatorin Inhibits TGF β 2-ERK Signaling to Suppress Esophageal Cancer Metastasis](https://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247500969&idx=1&sn=fdcaccdaba24f9c1a4ef6f64b2c5fe6a&scene=21#wechat_redirect)

作者在摘要部分写道:

> Gene Ontology analysis of The Cancer Genome Atlas (TCGA) gene expression datasets of ESCC patients with or without lympy metastasis identifies that *TGF β2* is highly enriched in the pathways essential for tumor metastasis and upregulates in the metastatic ESCC tumors. High *TGF β2* expression in ESCC correlates with metastasis and patient survival, and functionally contributes to tumor metastasis via activating extracellular signal-regulated kinases (ERK) signaling.

对有或无淋巴结转移的食管鳞癌患者的TCGA基因表达数据进行的GO分析表明，***TGF β2*在肿瘤转移所必需的通路中高度富集，并在转移性食管鳞癌中上调。食管鳞癌中*TGF β2*的高表达与肿瘤转移和患者生存期密切相关**，并通过激活细胞外信号调节激酶信号转导途径在功能上促进肿瘤转移。

接着，作者在**Results**的第一部分写道：

> To figure out the underlying mechanisms involved in ESCC invasion and metastasis,  
> RNA-sequencing data and clinical information of 60 ESCC cases were obtained from The Cancer Genome Atlas (TCGA) database,  
> and the gene profiles of tumors at N0 stage were compared with those at N3 stage.  
> Gene Ontology (GO) analysis of the differentially expressed genes indicated that a series of signaling pathways were involved in ESCC metastasis,  
> such as extracellular matrix organization (Figure 1A).  
> The frequency of each gene to be enriched in the pathways was calculated to identify the key drivers which affect most of the important signaling pathways involved in cancer invasion and metastasis.  
> Among the top genes highly enriched in the pathways listed in Figure 1A, *TGF β2*, which ranks 4th with a high frequency (26%) of enrichment in the total GO terms,  
> became our research focus (Figure 1B). As shown in Figure 1C,*TGF β2* had a significantly higher expression in the ESCC tumors with high metastasis compared with the tumors without metastasis (Figure 1C).  
> These analyses of TCGA data suggest that *TGF β2* may play a crucial role in metastasis of esophagus cancer.

为探讨食管癌侵袭转移的可能机制，从肿瘤基因组图谱(TCGA)数据库中获取了60例食管癌的RNA测序数据和临床资料，并比较了N0期和N3期肿瘤的基因图谱。  
差异表达基因的基因本体论(GO)分析表明，一系列信号通路参与食管癌转移，如细胞外基质组织(图1A)。  
计算每个基因在这些通路中富集的频率，以确定影响大多数涉及癌症侵袭和转移的重要信号通路的关键驱动因素。  
在图1A列出的途径中高度富集的top基因中，*TGF β2*成为我们的研究重点(图1B)，它排在第4位，在GO总条目中富集的频率很高(26%)。  
如图1C所示，*TGF β2*在高转移性食管鳞癌中的表达明显高于无转移者(图1C)。**这些结果提示*TGF β2*可能在食管癌的转移中起重要作用。**

作者为了说明**其所研究的分子（*TGF β2*）在食管鳞癌中很重要**，不惜在Figure1中用了A-M共13张图来说明这一点，这也是很多文章的套路：就是在Figure1中反复说明所研究分子的在所研究疾病中的重要性，其中最常见的两幅图，就是：

（1）分子在实验组和对照组高、低表达的箱线图：可以利用数据库数据，结合qPCR、WB等。  
（2）生存分析：同样可以利用数据库数据，或者自己收集的临床样本。  
（3）Figure 1B:  计算每个基因在这些通路中富集的频率，以确定影响大多数涉及癌症侵袭和转移的重要信号通路的关键驱动因素。  
在图1A列出的途径中高度富集的top基因中，*TGF β2*成为我们的研究重点(图1B)，它排在第4位，在GO总条目中富集的频率很高(26%)。

以上3步，给了我们无限思考和空间，这里我们重点讲如何利用数据库数据。

为什么要重点讲数据库的数据呢？因为以上3步，顺着走是“**说明所研究分子的在所研究疾病中的重要性**”，逆推就是“**当确定了研究疾病，但是还不知道研究什么分子和通路的时候，通过这种 data driven 的探索，可以很容易找到所研究疾病中的重要分子和通路，从而提出 hypothesis**”，这就比在海洋里的文献检索或者苦苦求人给个研究分子，来的更加有指导性，做起实验来也有的放矢，而且也不是所有人都有条件一上来就各种qPCR、WB的。

**但是，这与我们要讲的循环和批量有什么关系呢？有关，而且很有必要掌握这一技能**

试想一下，如果我们可以：

（1）写个循环，批量比较一下几万个基因里面，哪些基因在实验组 vs 对照组的比较中P值有统计学意义的（T test or Wilcoxon test），选择P值小于0.05的，**批量画箱线图（类似上面的Figure 1I）**。这一步其实有些类似于差异分析。但是有时候，差异分析中没有意义的基因（可能是logFC和矫正后的P值定的太过于严格），而T test or Wilcoxon test比较有意义的基因，在实验中却得到了验证。假设这一步找到了500个在实验组中高表达的基因（P值有统计学意义）。  
（2）用上面的500个在实验组高表达的基因，批量生存分析（单因素cox 或者 KM法），进一步缩小基因数目。  
（3）统计基因在GO或者KEGG通路中富集的频率，找top基因

以下开始，高分复现3步走！

#### 第1:差异分析

下面我们一步步来实现上面的操作，首先是基因在实验组 vs 对照组的表达量的比较及可视乎（箱线图）

为了方便，我直接去UCSC下载了食管癌的数据，建议到TCGA的GDC官网下载，关于[TCGA基础知识](https://mp.weixin.qq.com/s?__biz=MzI0NjUyMTE2MQ==&mid=2247484871&idx=2&sn=82adb7c4f72eba54a8085d1387572107&scene=21#wechat_redirect)，以及[GDC下载数据](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650733268&idx=1&sn=d5f9118fd480e9669e90ca923efb8ec8&scene=21#wechat_redirect)

文章中用了60例转移的数据，我这里直接用正常与肿瘤的173例数据

**如果是选择DESq2差异分析，可以看下代码，有些长，包含了前期的数据处理过程，不是这次讲述的重点，也可以跳过**

当然也可以仔细阅读，里面包含了数据清洗的过程和思考，而这些基本功其实很重要

```
rm(list = ls())  
library(tidyverse)  
options(stringsAsFactors = F)  
## 读取数据  
plat <- data.table::fread(file = "gencode.v22.annotation.gene.probeMap",data.table = F)  
exp_counts_data <- data.table::fread(file = "TCGA-ESCA.htseq_counts.tsv",data.table = F)  
  
##处理数据  
colnames(exp_counts_data)[1:10]  
colnames(plat)[1] <- c("Ensembl_ID")  
  
plat <- plat[,1:2]  
colnames(plat)  
  
exp_counts_data <- exp_counts_data %>%   
  inner_join(plat,by="Ensembl_ID") %>%   
  select(Ensembl_ID,gene,everything()) %>%   
  select(-Ensembl_ID) %>%  
  mutate(rowMean =rowMeans(.[grep("TCGA", names(.))])) %>% #求出平均数  
  arrange(desc(rowMean)) %>% #把表达量的平均值按从大到小排序  
  distinct(gene,.keep_all = T) %>% # gene留下第一个  
  select(-rowMean) %>% #反向选择去除rowMean这一列  
  column_to_rownames("gene")  
  
## 因为UCSC的数据是log2(count+1)，所以需要先取反，才能做差异分析  
fan_log2 <- function(data){  
  2^data - 1  
}  
exp_counts_data <- fan_log2(exp_counts_data)  
## 过滤低表达量的基因，保留至少在1个样本中都有表达的基因  
exp_counts_data <- exp_counts_data[apply(exp_counts_data,1, function(x) sum(x>1) > 1),]  
##报存一下数据用于差异分析  
exp_counts_data <- round(exp_counts_data,0)  
save(exp_counts_data,file = "exp_counts_data.Rdata")   
  
##用同样的方式对FPKM数据进行处理  
exp_fpkm_data <- data.table::fread(file = "TCGA-ESCA.htseq_fpkm.tsv",data.table = F)  
  
exp_fpkm_data <- exp_fpkm_data %>%   
  inner_join(plat,by="Ensembl_ID") %>%   
  select(Ensembl_ID,gene,everything()) %>%   
  select(-Ensembl_ID) %>%  
  mutate(rowMean =rowMeans(.[grep("TCGA", names(.))])) %>% #求出平均数  
  arrange(desc(rowMean)) %>% #把表达量的平均值按从大到小排序  
  distinct(gene,.keep_all = T) %>% # gene留下第一个  
  select(-rowMean) %>% #反向选择去除rowMean这一列  
  column_to_rownames("gene")  
  
## 因为UCSC的数据是log2(fpkm+1)，不用fpkm数据做差异，可以用log2(fpkm+1)做其他分析，可以不用还原，也可以还原，  
## 如果还原为fpkm，再取log2(fpkm)，为0的值会变成inf  
# fan_log2 <- function(data){  
#    2^data - 1  
#  }  
# exp_fpkm_data <- log2(exp_fpkm_data)  
# exp_fpkm_data <- fan_log2(exp_fpkm_data)  
  
## 过滤低表达量的基因，保留至少在1个样本中都有表达的基因  
exp_fpkm_data <- exp_fpkm_data[apply(exp_fpkm_data,1, function(x) sum(x>1) > 1),]  
  
save(exp_fpkm_data,file = "exp_fpkm_data.Rdata")   
  
##先读取临床分组数据  
phenotype <- data.table::fread(file = "TCGA-ESCA.GDC_phenotype.tsv",data.table = F)  
metadata <- data.frame(TCGA_id=phenotype$submitter_id.samples)   
##创建分组  
for (i in 1:nrow(metadata)) {  
  ## 指示  
  #i=1  
  print(i)  
  ## substring的用法，这是元素获取  
  num = as.numeric(substring(metadata[i,1],14,15))  
  #如果是肿瘤，就给第2列加上Tumor  
  if (num %in% seq(1,9)) {  
    metadata[i,2] = "Tumor"  
  }   
  #如果是正常组织，就给第2列加上Normal  
  if (num %in% seq(10,29)) {  
    metadata[i,2] = "Normal"  
  }   
}  
colnames(metadata) <- c("TCGA_id","sample")  
table(metadata$sample)  
#提取表达谱  
str(metadata$TCGA_id)  
table(metadata$TCGA_id %in% colnames(exp_counts_data))  
  
exp_counts_data <- as.data.frame(t(exp_counts_data))  
  
exp_counts_data <- exp_counts_data %>%   
  rownames_to_column("TCGA_id") %>%   
  inner_join(metadata,by = "TCGA_id") %>%   
  select(TCGA_id,sample,everything()) %>%   
  arrange(sample) ##按照分组排列样本   
  
metadata <- exp_counts_data[,1:2]  
table(metadata$sample)  
  
exp_counts_data <- exp_counts_data %>%   
  select(-sample) %>%   
  column_to_rownames("TCGA_id")  
  
exp_counts_data <- as.data.frame(t(exp_counts_data))  
  
##检查一下样本顺序  
identical(colnames(exp_counts_data),metadata$TCGA_id)  
  
exp_counts_data <- exp_counts_data %>%  
  rownames_to_column("TCGA_id")  
##最后是11例正常 vs 162例肿瘤 有表达谱和临床信息的食管癌  
  
## 差异分析  
metadata$sample <- factor(metadata$sample,levels = c("Normal","Tumor"),ordered = F)  
save(metadata,file = "metadata.Rdata") #保存一下分组文件  
  
library(DESeq2)  
### 第一列有名称，所以tidy=TRUE  
dds <-DESeqDataSetFromMatrix(countData=exp_counts_data,   
                             colData=metadata,   
                             design=~sample,  
                             tidy=T)  
nrow(dds)                                       
### 数据标准化用于看聚类  
### https://dwz.cn/xJTuI4aO  
### 很耗时间  
if(F){  
  vsd <- vst(dds, blind = FALSE)  
}  
  
### PCAf  
plotPCA(vsd, "sample")  
### 保存数据,可用于后续分析，如画热图等  
exprSet_vst <- as.data.frame(assay(vsd))  
test <- exprSet_vst[1:10,1:10]  
save(exprSet_vst,file = "exprSet_vst.Rdata")  
### Deseq2 更新后速度大幅度提升  
### https://dwz.cn/bb1jDs12  
if(F){  
  library(BiocParallel)  
  dds <- DESeq(dds,parallel = T)  
  save(dds,file="dds_very_long.Rdata")  
}  
  
load(file="dds_very_long.Rdata")  
  
### 提取标准化后的数据  
normalized_counts <- as.data.frame(counts(dds, normalized=TRUE))  
save(normalized_counts,file = "ESCA_normalized_counts.Rdata")  
### 单独作图简易展示  
plotCounts(dds, gene = "TGFB2", intgroup=c("sample"))  
### 还可以把数据返回  
plotdata <- plotCounts(dds, gene = "TGFB2", intgroup=c("sample"),returnData = T)  
library(ggplot2)  
ggplot(plotdata,aes(x=sample,y=count,col=sample))+  
  geom_jitter()+  
  theme_bw()  
  
### logFC矫正,注意顺序哈:?results()  
contrast <- c("sample","Tumor","Normal")  
dd1 <- results(dds, contrast=contrast, alpha = 0.05)  
plotMA(dd1, ylim=c(-5,5))  
### 如果发现样本需要做logFC校正  
dd2 <- lfcShrink(dds, contrast=contrast, res=dd1)  
plotMA(dd2, ylim=c(-5,5))  
summary(dd1, alpha = 0.05)  
  
### 导出差异分析的结果  
allDiff <- dd1 %>%   
  data.frame() %>%   
  rownames_to_column("gene_id")   
  
Diff_gene <- allDiff %>%   
  filter(abs(log2FoldChange) > 2) %>%  
  filter(pvalue < 0.05)  
save(Diff_gene,file = "Diff_gene.Rdata")  
##原文是仅用了logFC>1.2定义差异基因，这里我们以logFC>2 且矫正后P值小于0.05定义差异基因
```



**看了一下，TGF β2并不在上面这个差异基因列表里面，原因是我们定义的差异基因标准太过于严格了，这就有可能会漏掉一些重要的基因**，

我们用Wilcoxon test看看TGF β2是否表达有差异，答案是有的，这篇文章也证实了TGF β2在食管癌的转移中有重要作用  

**下面进入我们的重点，用循环，Wilcoxon test，批量比较几万个基因在正常 vs 肿瘤的表达是否有差异**

```
rm(list = ls())  
load(file = "exp_fpkm_data.Rdata") #用FPKM数据  
#load(file = "exprSet_vst.Rdata") 也可以用上面标准化的数据exprSet_vst  
load(file = "metadata.Rdata")  
colnames(metadata)[2] <- c("group")  
  
index <- as.character(metadata$TCGA_id)  
exp_fpkm_data <- exp_fpkm_data[,index]  
identical(colnames(exp_fpkm_data),metadata$TCGA_id)  
  
data <- as.data.frame(t(exp_fpkm_data))  
data <- data %>%   
  rownames_to_column("TCGA_id") %>%   
  inner_join(metadata,by = "TCGA_id") %>%   
  select(TCGA_id,group,everything())  
test <- data[1:10,1:10]  
  
#画图  
library(ggpubr)  
ggboxplot(  
  data, x = "group", y = "TGFB2",  
  color = "group", palette = c("#00AFBB", "#E7B800"),  
  add = "jitter"  
)+  
  stat_compare_means(method = "wilcox.test")
```

看一下数据长什么样

接着，我们开始循环比较，批量输出结果

使用lapply + function模式来是计算，[lapply 以及do.call 的介绍](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650734182&idx=1&sn=03f871b1b1d267f32181ce6d780a7247&scene=21#wechat_redirect)，lapply 三步走：

**第1,写出单次处理的function**

```
my.wilcox = function(x){  
  dd <- wilcox.test(data[,x] ~ group, data = data)  
  data.frame(gene=x,p.value=dd$p.value)  
}  
### 测试函数功能  
my.wilcox("TGFB2")
```

**第2步lapply批量作用于函数，返回list，为了方便，我们先用100基因试试**

```
lapplylist = lapply(colnames(data)[-c(1:2)][1:100],my.wilcox)
```

**第3步do.call 转换list**

```
wilcox_data <- do.call(rbind,lapplylist)
```

**如果熟练了，三步走可以变成一步**

```
wilcox_data <- do.call(rbind,lapply(colnames(data)[-c(1:2)][1:100],function(x){  
  dd <- wilcox.test(data[,x] ~ group, data = data)  
  data.frame(gene=x,p.value=dd$p.value)  
}))
```

**速度再快一些, 变成future\_lapply + funcxtion**

```
### 依然是lapply 三步走，只有一点点不一样  
library(future.apply)  
plan(multisession)  
  
### 第2步lapply批量作用于函数，返回list  
### system.time(lapplylist = lapply(colnames(data)[-c(1:2)][1:100],my.wilcox))  
system.time(lapplylist <- future_lapply(colnames(data)[-c(1:2)][1:100],my.wilcox))  
### 第3步do.call 转换list  
wilcox_data <- do.call(rbind,lapplylist)  
  
##写成一步，对所用基因循环，你自己运行的时候，把if (F) 里面的F改为T就可  
if (F) {  
  wilcox_data <- do.call(rbind,future_lapply(colnames(data)[-c(1:2)],function(x){  
    dd <- wilcox.test(data[,x] ~ group, data = data)  
    data.frame(gene=x,p.value=dd$p.value)  
  }))  
  save(wilcox_data,file = "wilcox_data.Rdata")  
}  
load(file = "wilcox_data.Rdata")  
##挑出出p值显著的  
wilcox_data_P <- wilcox_data %>%   
  filter(p.value < 0.01) %>%   
  arrange(p.value) #根据p值排序  
dim(wilcox_data_P)  
#[1] 8094    2
```

8094个P值显著的基因，比差异分析多了很多（当然可能与我们用FPKM数据，而差异分析用的是count数据，这也会引起不同），

接着画图和批量输出

```
##画图  
myboxplot <- function(gene){  
  ggboxplot(  
    data, x = "group", y = gene,  
    color = "group", palette = c("#00AFBB", "#E7B800"),  
    add = "jitter"  
  )+  
    stat_compare_means(method = "wilcox.test")  
}  
myboxplot("C19orf47")  
  
### 如何导出图片  
dir.create("output")  
inputgene="C19orf47"  
p = myboxplot(inputgene)  
ggsave(p,filename = paste0("output/",inputgene,".pdf"), width = 6, height = 6)  
  
## 批量导出  
datasub <- c(as.character(wilcox_data_P$gene[1:100]))  
for (i in 1:length(datasub)){  
  ## 1.指示  
  #i=1  
  print(i)  
  ## 2.计算  
  inputgene = datasub[i]  
  p = myboxplot(inputgene)  
  ggsave(p,filename = paste0("output/",inputgene,".pdf"), width = 12, height = 9)  
}
```

还可以把多张图画在同一张Figure上

```
your_plot <- list()  
for (j in 1:length(datasub)) {  
  #画图  
  p <- ggboxplot(  
    data, x = "group", y = datasub[j],  
    color = "group", palette = c("#00AFBB", "#E7B800"),  
    add = "jitter"  
  )+  
    stat_compare_means(method = "wilcox.test")  
  # 把图保存在list里  
  your_plot[[j]] <- p  
}  
##cowplot拼图  
library(cowplot)  
PLOT <- plot_grid(plotlist = your_plot,ncol = 5 ,align = "hv") ##一行放5个图，假设每个小图图定为高4，宽4  
##计算高度  
height <- length(your_plot)/4*4  
##保存图片  
ggsave(PLOT,filename = paste0("output/","cow_boxplot",".pdf"),  
       limitsize = FALSE,width = 20,height = height)  
##共100个图，每9个保存为一个图试试  
for (i in seq(9,length(datasub),9)) {  
  print(i)  
  ##切分起始位置  
  beginning <- i - 8  
  ##1.切分your_plot  
  all_list <- your_plot[beginning:i]  
  ##2.拼图，并且加上ABCD等标签  
  all_plot <- plot_grid(plotlist = all_list,ncol = 3 ,labels = LETTERS[1:9],align = "hv") ##一行放3个图,每个小图图定为高4，宽4  
  ##3.批量输出和保存  
  ggsave(all_plot,  
         filename = paste0("output/",beginning," to ",i,".pdf"),  
         width = 12,  
         height = 12)  
}  
  
##同样，以上可以写成函数  
datasub <- c(as.character(wilcox_data_P$gene[1:100]))  
dir.create("aa.output")  
#同样可以写成函数  
gene.boxplot <- function(datasub){  
  your_plot <- list()  
  for (j in 1:length(datasub)) {  
    # 绘图  
    p <- ggboxplot(  
      data, x = "group", y = datasub[j],  
      color = "group", palette = c("#00AFBB", "#E7B800"),  
      add = "jitter"  
    )+  
      stat_compare_means(method = "wilcox.test")  
    # 保存在list里  
    your_plot[[j]] <- p  
  }  
  
  for (i in seq(9,length(datasub),9)) {  
    print(i)  
    ##切分起始位置  
    beginning <- i - 8  
    ##1、切分your_plot  
    all_list <- your_plot[beginning:i]  
    # 2、拼图,并且加上ABCD等标签  
    all_plot <- plot_grid(plotlist = all_list,ncol = 3 ,labels = LETTERS[1:9],align = "hv") ##一行放3个图,每个小图图定为高4，宽4  
    # 3、保存图片  
    ggsave(all_plot,  
           filename = paste0("aa.output/",beginning," to ",i,".pdf"),  
           width = 12,  
           height = 12)  
  }  
}  
##测试函数功能  
gene.boxplot(datasub)
```

此外，也可以选择差异分析的上调基因来批量画箱线图，孰高孰低，一目了然，

#### 第2:批量生存分析

**接着，就是高表达基因的批量生存分析了，以进一步缩小基因范围**

**批量进行单变量cox回归**

```
rm(list = ls())  
load(file = "exp_fpkm_data.Rdata") #用FPKM数据  
load(file = "metadata.Rdata")#上面的分组数据  
load(file = "wilcox_data.Rdata") #上面wilcox test的数据  
  
##挑出出p值显著的  
wilcox_data_P <- wilcox_data %>%   
  filter(p.value < 0.01) %>%   
  arrange(p.value) #根据p值排序  
#加载生存数据  
survival_data <- data.table::fread(file = "TCGA-ESCA.survival.tsv",data.table = F)  
colnames(metadata) <- c("sample","group")  
#提取p值显著的基因的表达谱  
index <- as.character(wilcox_data_P$gene)  
exp_fpkm_data <- exp_fpkm_data[index,]  
#转置  
data <- as.data.frame(t(exp_fpkm_data))  
test <- data[1:10,1:10]  
#合并临床信息与基因表达数据  
data <- data %>%   
  rownames_to_column("sample") %>%   
  inner_join(metadata,by = "sample") %>%  
  inner_join(survival_data,by="sample") %>%   
  select(-`_PATIENT`) %>%   
  filter(group == "Tumor") %>%  #选择肿瘤  
  select(sample,group,OS,OS.time,everything())  
test <- data[1:10,1:10]  
data$OS.time <- round(data$OS.time/30,2) #时间转为月份
```

有了上面这个清洁数据，就可以做批量生存分析了

```
##处理一下，不然会报错  
colnames(data) <- gsub("-","_",colnames(data))  
#genes <- colnames(data)[-c(1:4)]  
#genes[707]，为"5S-rRNA"，数字开头，会报错；加上前4列临床信息就是第711列  
#[1] "5S-rRNA"  
genes <- colnames(data)[-c(1:4,711)]  
  
library(survival)  
##批量生存分析  
res <- data.frame()  
for (i in 1:length(genes)) {  
  print(i)  
  surv =as.formula(paste('Surv(OS.time, OS)~', genes[i]))  
  x = coxph(surv, data = data)  
  x = summary(x)  
  p.value=signif(x$wald["pvalue"], digits=2)  
  HR =signif(x$coef[2], digits=2);#exp(beta)  
  HR.confint.lower = signif(x$conf.int[,"lower .95"], 2)  
  HR.confint.upper = signif(x$conf.int[,"upper .95"],2)  
  CI <- paste0("(",   
               HR.confint.lower, "-", HR.confint.upper, ")")  
  res[i,1] = genes[i]  
  res[i,2] = HR  
  res[i,3] = CI  
  res[i,4] = p.value  
}  
names(res) <- c("ID","HR","95% CI","p.value")  
res <- res %>%   
  filter(p.value < 0.05) #选出P值有意义的,524个  
save(res,file = "res_HR.Rdata")
```

**同样上述也可以写成函数，以后可以直接用函数，速度更快**

```
##处理一下，不然会报错  
#colnames(data) <- gsub("-","_",colnames(data))  
#genes <- colnames(data)[-c(1:4,711)]  
#genes[707]  
library(survival)  
##1.写函数  
your.survival <- function(genes,data){  
  print(genes)  
  surv =as.formula(paste('Surv(OS.time, OS)~', genes))  
  x = coxph(surv, data = data)  
  x = summary(x)  
  p.value=signif(x$wald["pvalue"], digits=2)  
  HR =signif(x$coef[2], digits=2);#exp(beta)  
  HR.confint.lower = signif(x$conf.int[,"lower .95"], 2)  
  HR.confint.upper = signif(x$conf.int[,"upper .95"],2)  
  CI <- paste0("(",   
               HR.confint.lower, "-", HR.confint.upper, ")")  
  data.frame(ID=genes,HR=HR,CI_95=CI,p.value=p.value)  
}  
  
##测试函数  
your.survival("TFDP1", data = data)  
###2.第2步lapply批量作用于函数，返回list  
lapplylist = lapply(genes[1:100],your.survival,data = data)  
###3.第3步do.call 转换list  
cox_data <- do.call(rbind,lapplylist)  
  
library(future.apply)  
plan(multisession)  
### 第2步lapply批量作用于函数，返回list  
system.time(lapplylist <- future_lapply(genes,your.survival,data = data))  
# 用户  系统  流逝   
# 1.17  1.12 13.83   
##可以看出，速度大大提高了  
### 第3步do.call 转换list  
cox_data <- do.call(rbind,lapplylist)  
  
##一步到位写成，就是  
if (F) {  
  cox_data <- do.call(rbind,future_lapply(genes,data=data,function(genes,data){  
    print(genes)  
    surv =as.formula(paste('Surv(OS.time, OS)~', genes))  
    x = coxph(surv, data = data)  
    x = summary(x)  
    p.value=signif(x$wald["pvalue"], digits=2)  
    HR =signif(x$coef[2], digits=2);#exp(beta)  
    HR.confint.lower = signif(x$conf.int[,"lower .95"], 2)  
    HR.confint.upper = signif(x$conf.int[,"upper .95"],2)  
    CI <- paste0("(",   
                 HR.confint.lower, "-", HR.confint.upper, ")")  
    data.frame(ID=genes,HR=HR,CI_95=CI,p.value=p.value)  
  }))  
  row.names(cox_data) <- cox_data[,1]  
  cox_data <- cox_data %>%   
    filter(p.value < 0.05) #选出P值有意义的,同样是524个  
  save(cox_data,file = "cox_data.Rdata")  
}  
load(file = "cox_data.Rdata")
```

**批量进行KM法生存分析，批量输出生存曲线**

**首先是surv\_cutpoint()函数寻找最佳cutoff值分组，这个需求挺多人问过，[关于寻找最佳cutoff值分组的几种方法](https://mp.weixin.qq.com/s?__biz=MzI0NjUyMTE2MQ==&mid=2247485276&idx=2&sn=70b03e2f9d269d07f48a1c48240c8428&scene=21#wechat_redirect)，可以的看看这个帖子**

```
library(survival)  
library(survminer)  
##处理一下列名,不然这些列不会被切割  
#colnames(data) <- gsub("-","_",colnames(data))  
#data <- data[,-711]  
res.cut <- surv_cutpoint(data, time = "OS.time",   
                         event = "OS",   
                         variables = names(data)[5:ncol(data)],   
                         minprop = F)   
res.cat <- surv_categorize(res.cut)      
test <- res.cat[1:10,1:10]  
###也可以使用median来批量做  
###鉴于好多文献用这种surv_cutpoint方法寻找最佳cutoff值，这次演示用  
genes <- colnames(data)[-c(1:4)]  
res2 <- data.frame()  
for (i in 1:length(genes)) {  
  print(i)  
  surv =as.formula(paste('Surv(OS.time, OS)~', genes[i]))  
  x = survdiff(surv, data = res.cat)  
  pValue=1-pchisq(x$chisq,df=1)  
  res2[i,1] = genes[i]  
  res2[i,2] = pValue  
}  
names(res2) <- c("ID","pValue_log")  
res2 <- res2 %>%   
  filter(pValue_log < 0.05) #4568个，非常多  
save(res2,file = "res2.Rdata")
```

**同样，上面也可以写成函数，以后可以直接用函数，速度更快**

```
##同样是先切割数据  
res.cut <- surv_cutpoint(data, time = "OS.time",  
                         event = "OS",  
                         variables = names(data)[5:ncol(data)],  
                         minprop = F)  
res.cat <- surv_categorize(res.cut)  
test <- res.cat[1:10,1:10]  
## 1.写函数  
km.survival <- function(genes,data){  
  print(genes)  
  surv =as.formula(paste('Surv(OS.time, OS)~', genes))  
  x = survdiff(surv, data = res.cat)  
  pValue=1-pchisq(x$chisq,df=1)  
  data.frame(ID=genes,pValue.log=pValue)  
}  
## 2.测试数据  
km.survival("TFDP1", data=res.cat)  
## 3.lapply  
lapplylist<- lapply(genes[1:100],km.survival,data = res.cat)  
## 4.do.call合并  
km_data <- do.call(rbind,lapplylist)  
## 5.future.apply更快  
library(future.apply)  
plan(multisession)  
system.time(lapplylist <- future_lapply(genes,km.survival,data = res.cat))  
# 用户  系统  流逝   
# 4.35  2.59 10.59  
km_data <- do.call(rbind,lapplylist) #do.call合并  
  
## 6.一步到位  
if (F) {  
  km_data <- do.call(rbind,future_lapply(genes,data=res.cat,function(genes,data){  
    print(genes)  
    surv =as.formula(paste('Surv(OS.time, OS)~', genes))  
    x = survdiff(surv, data = res.cat)  
    pValue=1-pchisq(x$chisq,df=1)  
    data.frame(ID=genes,pValue.log=pValue)  
  }))  
  row.names(km_data) <- km_data[,1]  
  km_data <- km_data %>%   
    filter(pValue.log < 0.05)  
  save(km_data,file = "km_data.Rdata")  
}  
load(file = "km_data.Rdata")  
  
##可以与上面的单变量cox的取交集  
survival_cox_km <- cox_data %>%   
  inner_join(km_data,by="ID") ##515个  
save(survival_cox_km,file = "survival_cox_km.Rdata")
```

**接着，对上述基因，批量输出生存曲线**

```
rm(list = ls())  
load(file = "survival_cox_km.Rdata")  
load(file = "suivival.Rdata")  
colnames(data) <- gsub("-","_",colnames(data))  
  
table(survival_cox_km$ID %in% colnames(data))  
str(survival_cox_km$ID)  
  
survival_cox_km$ID <- as.character(survival_cox_km$ID)  
index <- survival_cox_km$ID  
sur_data <- data[,index]  
sur_data <- cbind(data[,1:4],sur_data)
```

**有了这个规则的清洁数据，我们就可以批量做生存曲线了**，

首先还是surv\_cutpoint()函数寻找最佳cutoff值分组，生成画生存曲线的分组数据

```
rm(list = ls())  
library(survival)  
library(survminer)  
load(file = "survival_cox_km.Rdata")  
load(file = "suivival.Rdata")  
colnames(data) <- gsub("-","_",colnames(data))  
table(survival_cox_km$ID %in% colnames(data))  
str(survival_cox_km)  
survival_cox_km$ID <- as.character(survival_cox_km$ID)  
index <- survival_cox_km$ID  
sur_data <- data[,index]  
sur_data <- cbind(data[,1:4],sur_data)  
str(sur_data)  
sur_data <- sur_data %>%  
  column_to_rownames("sample") %>%  
  select(-group)  
res.cut <- surv_cutpoint(sur_data, time = "OS.time",  
                         event = "OS",  
                         variables = names(sur_data)[3:ncol(sur_data)],  
                         minprop = F)  
res.cat <- surv_categorize(res.cut)
```

**现在分组数据也有了，万事俱备，开始批量画生存曲线，[关于生存曲线及临床建模](https://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247504005&idx=1&sn=429be8c4b22757329f6b1c6e7dc5bd41&scene=21#wechat_redirect)，我在B站也分享过**

```
##1.写函数  
genes <- colnames(res.cat)[-c(1:2)]  
#genes <- colnames(sur_data)[-c(1:2)] #也可以，一样的  
  
your.surv <- Surv(res.cat$OS.time, res.cat$OS) ##要放在函数或者循环的外面，不然会报下面的错误  
# Error in eval(inp, data, env) : 找不到对象'your.surv'  
# Timing stopped at: 0.58 0.22 3.25  
  
your.km.plot <- function(genes,data){  
  #genes <- "GZF1"  
  print(genes)  
  group <- res.cat[,genes] #分组  
  survival_dat <- data.frame(group = group)  
  #为了下面画生存的颜色和分组不会搞反，因子化分组顺序  
  group <- factor(group, levels = c("low", "high"))   
  fit <- survfit(your.surv ~ group)  
  # log-rank test：pvalue  
  # This function implements the G-rho family of Harrington and Fleming (1982), with weights on each death of S(t)^rho, where S is the Kaplan-Meier estimate of survival.   
  # With rho = 0 this is the log-rank or Mantel-Haenszel test, and with rho = 1 it is equivalent to the Peto & Peto modification of the Gehan-Wilcoxon test.  
  sdf <- survdiff(your.surv ~ group,rho=0)  
  p.val <- 1 - pchisq(sdf$chisq, length(sdf$n)-1)  
  p.val  
  photo2 <-  ggsurvplot(fit,data = survival_dat, #这里很关键，不然会报错  
                        legend.title = genes,#定义图例的名称  
                        legend.labs = c("low","high"), #所以上面要因子化分组顺序  
                        #legend = "top",#图例位置  
                        pval = T, #在图上添加log rank检验的p值  
                        #pval.method = TRUE,#添加p值的检验方法  
                        #conf.int = TRUE,#添加置信区间  
                        risk.table = TRUE, #在图下方添加风险表  
                        #risk.table.col = "strata", #根据数据分组为风险表添加颜色  
                        risk.table.y.text = F,#风险表Y轴是否显示分组的名称,F为以线条展示分组  
                        #linetype = "strata", #改变不同组别的生存曲线的线型  
                        #surv.median.line = "hv", #标注出中位生存时间  
                        xlab = "Time in years", #x轴标题  
                        xlim = c(0,max(res.cat$OS.time)), #展示x轴的范围  
                        break.time.by = 10, #x轴间隔  
                        size = 1.5, #线条大小  
                        #ggtheme = theme_bw(), #为图形添加网格  
                        palette = c("#00BFFF","#DAA520")#图形颜色风格  
  )   
  
  photo2  #看一下图  
  # 修改图例  
  # 修改风险表的图例名称   
  photo2$table <- photo2$table + labs(  
    title = "Number at risk")  
  # Changing the font size, style and color of photo2  
  # survival curves, risk table  
  photo2 <- ggpar(  
    photo2,  
    font.title= c(16, "bold", "darkblue"),#16号字体，粗体，darkblue色  
    font.x = c(14, "bold.italic", "red"),#14号字体，粗斜体，red  
    font.y = c(14, "bold.italic", "darkred"), #14号字体，粗斜体，darkred  
    font.xtickslab = c(12, "plain", "darkgreen"),#调整X轴上字体大小、颜色和风格  
    legend = "top" #图例的位置  
  )  
  photo2  #再看一下图  
}  
  
##2.测试函数功能  
your.km.plot("ESM1",data = res.cat)  
##3.lappy  
lapplylist = lapply(genes[1:100],your.km.plot,data = res.cat)  
###4.future_lapply  
library(future.apply)  
plan(multisession)  
system.time(lapplylist <- future_lapply(genes[1:100],your.km.plot,data = res.cat))  
#用户 系统 流逝   
#1.42 0.27 7.29   
  
##批量输出图  
dir.create("surv.output")  
### 如何导出图片  
inputgene="ESM1"  
p = your.km.plot(inputgene,data = res.cat)  
library(patchwork)  
patchwork <- (p$plot/p$table) + plot_layout(nrow =2, heights = c(4, 2)) #生存曲线高度4成,table表2  
patchwork  
ggsave(plot = patchwork,filename = paste0("surv.output/",inputgene,".pdf"), width = 6, height = 6)  
  
## 批量导出  
datasub <- c(as.character(genes[1:10]))  
for (i in 1:length(datasub)){  
  ## 1.指示  
  #i=1  
  print(i)  
  ## 2.计算  
  inputgene = datasub[i]  
  p = your.km.plot(inputgene,data = res.cat)  
  library(patchwork)  
  #为了把生存曲线与曲线下的风险表画在一起  
  patchwork <- (p$plot/p$table) + plot_layout(nrow =2, heights = c(6, 2)) #生存曲线高度6成,table表2成  
  patchwork  
  ggsave(plot = patchwork,filename = paste0("surv.output/",inputgene,".pdf"), width = 8, height = 8)  
}
```

一下子这100个基因的生存曲线就出来了

**还可以把多张生存曲线图打印在同一张figure上**

```
##画100个基因的图，每9个保存为一个figure试试  
library(future.apply)  
plan(multisession)  
system.time(lapplylist <- future_lapply(genes[1:100],your.km.plot,data = res.cat))  
datasub <- c(as.character(genes[1:100]))  
library(cowplot)  
for (i in seq(9,length(datasub),9)) {  
  print(i)  
  ##切分起始位置  
  beginning <- i - 8  
  ##1.切分your_plot  
  all_list <- lapplylist[beginning:i]  
  ##2.拼图，并且加上ABCD等标签  
  all_plot <- arrange_ggsurvplots(all_list,print = F,ncol = 3, nrow = 3,  
                                  risk.table.height = 0.3,  
                                  surv.plot.height = 0.7)  
  ##3.批量输出和保存  
  ggsave(all_plot,  
         filename = paste0("surv.output/",beginning," to ",i,".pdf"),  
         width = 18,  
         height = 18)  
}
```

把生存曲线一下子就画在同一个figure上了

#### 第3:统计基因频率

**GO和KEGG分析条目中基因频率统计，依旧是循环实现**

```
rm(list = ls())  
library(tidyverse)  
#加载数据  
load(file = "survival_cox_km.Rdata")   
##注意基因名称要修改回来  
survival_cox_km$ID <- gsub("_","-",survival_cox_km$ID)  
##加载logfc的数据，后面画好看的图  
load(file = "allDiff.Rdata")  
allDiff_gene <- allDiff[,c("gene_id","log2FoldChange","padj")]  
colnames(allDiff_gene)[1] <- c("ID")  
##合并数据,有logfc，有单变量cox的p.value和HR,有KM分析的log-rank检验p值  
allDiff_gene <- allDiff_gene %>%  
  inner_join(survival_cox_km,by = "ID")
```

GO分析，用这上面的基因来做GO和KEGG

```
#获得基因列表  
gene <- as.character(allDiff_gene$ID)  
#基因名称转换，返回的是数据框  
library(clusterProfiler)  
gene = bitr(gene, fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")  
##GO分析  
if(F){  
  go <- enrichGO(gene = gene$ENTREZID, OrgDb = "org.Hs.eg.db", ont="all")  
}  
## readable = TRUE或者setReadable()函数可以将ENTREZIDz转换回symbol  
go<-setReadable(go,OrgDb = "org.Hs.eg.db")  
save(go,file="go.Rdata")  
load(file="go.Rdata")  
p <- barplot(go, split="ONTOLOGY") +facet_grid(ONTOLOGY~., scale="free")  
p
```

**接着，重点来了，GO条目中基因频率统计**：

1.首先确定框架，我们想重复的操作是什么？

2.单次操作应该如何做

3.如何用R语言实现单次的需求

```
symboldata <- as.data.frame(go)  
### 先尝试修改其中一个  
test = symboldata$geneID[1]  
test  
### 需要裂解  
unlist(strsplit(test,split = "/"))  
  
### 1.创建容器,此处是向量  
splitvector <- c()  
### 2.循环操作导出到容器  
for(i in 1:length(symboldata$geneID)){  
  print(i)  
  new = unlist(strsplit(symboldata$geneID[i],split = "/"))  
  splitvector = c(splitvector,new)  
}  
  
### 统计频次  
table(splitvector)  
### 排序  
sortdata = sort(table(splitvector),decreasing = T)  
### 成数据框来查看  
test <- as.data.frame(sortdata)  
write.csv(test,file = "GO.term_gene.freq.csv")
```

如果觉得上面的GO分析图不够好看，想自定义更漂亮的，也可以，

**注：以下代码参考自生信技能树健明老师的教程，源代码在健明老师的GitHub的GEO教程可以找到**

```
###画更好看的通路图  
deg <- allDiff_gene %>%   
  column_to_rownames("ID")  
head(deg)  
## 不同的阈值，筛选到的差异基因数量就不一样，后面的超几何分布检验结果就大相径庭。  
logFC_t=0  
deg$g=ifelse(deg$padj > 0.05,'stable',  
             ifelse( deg$log2FoldChange > logFC_t,'UP',  
                     ifelse( deg$log2FoldChange < -logFC_t,'DOWN','stable') ))  
table(deg$g)  
head(deg)  
deg$symbol=rownames(deg)  
library(ggplot2)  
library(clusterProfiler)  
library(org.Hs.eg.db)  
df <- bitr(unique(deg$symbol), fromType = "SYMBOL",  
           toType = c( "ENTREZID"),  
           OrgDb = org.Hs.eg.db)  
head(df)  
DEG=deg  
head(DEG)  
  
DEG=merge(DEG,df,by.y='SYMBOL',by.x='symbol')  
head(DEG)  
#save(DEG,file = 'anno_DEG.Rdata')  
  
gene_up= DEG[DEG$g == 'UP','ENTREZID']   
gene_down=DEG[DEG$g == 'DOWN','ENTREZID']   
gene_diff=c(gene_up,gene_down)  
gene_all=as.character(DEG[ ,'ENTREZID'] )  
data(geneList, package="DOSE")  
head(geneList)  
boxplot(geneList)  
boxplot(DEG$log2FoldChange)  
  
go.up <- enrichGO(gene = gene_up,  
                  OrgDb = "org.Hs.eg.db",   
                  ont="all",  
                  universe = gene_all,  
                  pvalueCutoff = 0.04, ##根据具体情况调整  
                  qvalueCutoff =0.04)  ####根据具体情况调整  
head(go.up)[,1:6]  
dotplot(go.up )  
#ggsave('go.up.dotplot.pdf')  
go.down <- enrichGO(gene = gene_down,  
                    OrgDb = "org.Hs.eg.db",   
                    ont="all",  
                      universe = gene_all,  
                      pvalueCutoff = 0.9, ##根据具体情况调整  
                      qvalueCutoff =0.9)  ##根据具体情况调整  
head(go.down)[,1:6]  
dotplot(go.down )  
#ggsave('go.down.dotplot.pdf')  
go.diff <- enrichGO(gene = gene_diff,  
                    OrgDb = "org.Hs.eg.db",   
                    ont="all",  
                    universe = gene_all,  
                    pvalueCutoff = 0.05, ##根据具体情况调整  
                    qvalueCutoff =0.05)  ##根据具体情况调整  
head(go.diff)[,1:6]  
dotplot(go.diff )  
#ggsave('go.diff.dotplot.pdf')  
  
go_diff_dt <- as.data.frame(go.diff)  
go_down_dt <- as.data.frame(go.down)  
go_up_dt <- as.data.frame(go.up)  
down_go<-go_down_dt[go_down_dt$pvalue<0.05,]  
down_go$group=-1  
up_go<-go_up_dt[go_up_dt$pvalue<0.05,]  
up_go$group=1
```

**加载画图函数，这个函数是健明老师2018年随手写的一个画图函数，真是厉害，把上调和下调基因的富集分开绘制，**

我努力尝试调整一下，并与健明老师进行了沟通

```
source('functions.R')  
go_figure=go.kegg_plot(up.data=up_go,down.data=down_go)  
print(go_figure)  
ggsave(go_figure,filename = 'GO_up_down.pdf')
```

  
这个GO图,左边的英文名称代表差异基因富集到的 GO Terms，X轴表示-log10(dat$pvalue)乘上分组,  
如：橙色的GO terms（其X轴大于0），表示上调基因富集的条目,X轴越大pvalue越显著；  
蓝色的GO terms（其X轴小于0），表示下调基因富集的条目，X轴越小pvalue越显著

同理，GSEA

```
kk_gse <- gseKEGG(geneList     = geneList,  
                  organism     = 'hsa',  
                  nPerm        = 1000,  
                  minGSSize    = 70,  
                  pvalueCutoff = 0.05, ##根据具体情况调整  
                  verbose      = FALSE)  
head(kk_gse)[,1:6]  
gseaplot(kk_gse, geneSetID = rownames(kk_gse[1,]))  
  
down_kegg<-kk_gse[kk_gse$pvalue<0.05 & kk_gse$enrichmentScore < 0,]  
down_kegg$group=-1  
up_kegg<-kk_gse[kk_gse$pvalue<0.05 & kk_gse$enrichmentScore > 0,]  
up_kegg$group=1  
  
g_kegg=go.kegg_plot(up_kegg,down_kegg)  
print(g_kegg)  
ggsave(g_kegg,filename = 'kegg_up_down_gsea.pdf')
```

这个KEGG图,左边的英文名称代表差异基因富集到的通路，X轴表示-log10(pvalue)乘上分组  
如：橙色的通路（其X轴大于0）,表示上调基因富集的通路，X轴越大pvalue越显著；蓝色的通路（其X轴小于0），表示下调基因富集的通路，X轴越小pvalue越显著

---

**至此，这篇文章的几种方法已经复现完毕，这个思路就可以用到很多干湿结合的文章中去，找分子，找思路。**  
**总结一下，就是：高表达、预后差、富集分析top基因**。这三个过程都可以批量，开启上帝视觉，为实验节约资源并提供方向  
当然，我们只是用了个别的思路，还有很多的思路，**技能掌握了+看文献找思路+动手实现在自己的课题**  
例如：

1.  [跟Nature一起学习TCGA,GTEx和CCLE数据库的使用](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650733992&idx=1&sn=7465a9d9d26e9f0d8e23d0ff032fe1f4&scene=21#wechat_redirect "跟Nature一起学习TCGA,GTEx和CCLE数据库的使用")
    
2.  [单基因批量相关性分析的妙用](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650733008&idx=1&sn=b66e3fd527f99ddf19dcf6c2501e5be3&scene=21#wechat_redirect "单基因批量相关性分析的妙用")
    
3.  [又是神器！基于单基因批量相关性分析的GSEA](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650733734&idx=1&sn=4fa58cdcde1d908588f28d859aaddfaa&scene=21#wechat_redirect "又是神器！基于单基因批量相关性分析的GSEA")
    

……还有很多，技能掌握了，用的就越灵活和得心应手。

---

### 二、万物皆可批量

果子老师在[循环与批量的课程中](https://mp.weixin.qq.com/s?__biz=MzIyMzA2MTcwMg==&mid=2650735312&idx=1&sn=f5112522e84e6ca17fb79cf5fbf5da22&scene=21#wechat_redirect "循环与批量的课程中")，总结了三步走思路，真的是太实用，一下子打开了闸门  
从上面反复循环、函数+循环的训练中，我写的很慢，细分为了6步：

1.  **写函数**
    
2.  **测试函数**
    
3.  **lapply**
    
4.  **do.call合并**
    
5.  **future\_lapply更快**
    
6.  **尝试一步到位**
    

反复练习以上6步一段时间，相信很快可以上手，做很多事情都可以尝试去写函数，需要反复的就写循环，循环和批量是学习R语言进阶的一个很大的挑战，也是一个很明确的瓶颈。

---

### 三、一些感想

从2019年09月底线下大课，从[GZ01到目前GZ07](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIyMzA2MTcwMg==&action=getalbum&album_id=1336377223624065025&scene=173&from_msgid=2650735312&from_itemidx=1&count=3&nolastread=1&uin=&key=&devicetype=Windows+10+x64&version=6302019c&lang=zh_CN&ascene=0&fontgear=2 "GZ01到目前GZ07") 系列课程，快两年时间了，果子老师陪伴了我从启蒙、入门、成长的R语言和生信学习过程，一路上给了我非常多的鼓励、帮助和支持，既是我的老师，更是我的兄长，感恩又感激！！

接到果子老师邀请写推文的一刻，我既开心又激动，一直想了很久，应该怎么去开展这个写作，花了一个星期，终于要写完了，也有些不舍！  
在写这个推文的过程中，我自己的收获也是很大，藉此机会，我回头梳理了和总结了这两年的一些学习内容，仿佛冲破了一些瓶颈！

更重要的是，结合这段时间以来，我的两位导师的询询教导，我找到了适合自己未来发展的科研方向：**从data driven到hypothesis driven的科研体系**  
当然，这两者之间的跨越，**需要立足于深厚的研究背景知识以及临床经验积累**，而这些恰恰是我目前所匮乏的，也是未来我需要深耕的。  
最后，感谢我的两位导师在我前行路上的鼓励、教导和指引，很幸运遇上了两位老师！！