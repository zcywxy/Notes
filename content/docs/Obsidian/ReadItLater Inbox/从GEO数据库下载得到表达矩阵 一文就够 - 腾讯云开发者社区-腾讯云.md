[[ReadItLater]] [[Article]]

# [从GEO数据库下载得到表达矩阵 一文就够 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1078345)

在第一讲我们详细介绍了GEO数据库的基础知识及规律，也了解了如何利用官方R包`GEOquery`来探索GEO数据库，当然，我的生信菜鸟团博客里面也从很多其它角度解析过它，欢迎大家自行搜索学习。总得来说，从GEO数据库里面得到感兴趣数据集的表达矩阵分成两类，最简单的就是直接下载作者归一化好的表达矩阵咯，比较麻烦的就是下载最原始芯片数据，然后根据不同的芯片来一一解读成表达矩阵。

[解读GEO数据存放规律及下载，一文就够](https://cloud.tencent.com/developer/article/1078339?from=10680)

[解读SRA数据库规律一文就够](http://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247486054&idx=1&sn=209975adee162228cfe6e6c5065c5c8c&chksm=9b484addac3fc3cb95a266affc681050381091616ed265445cf364ef0a7cb24b8c2bf5878090&scene=21#wechat_redirect)

##  **直接下载数据集作者上传的表达矩阵**

通常我们默认作者对其芯片数据处理的步骤是正确的，所以稍微掌握技巧即可下载其归一化的表达矩阵。

而且，我已经把下载GEO数据集的表达矩阵这个过程包装成了函数，如下：

```
downGSE <- function(studyID = "GSE1009", destdir = ".") {

    library(GEOquery)
    eSet <- getGEO(studyID, destdir = destdir, getGPL = F)

    exprSet = exprs(eSet[[1]])
    pdata = pData(eSet[[1]])

    write.csv(exprSet, paste0(studyID, "_exprSet.csv"))
    write.csv(pdata, paste0(studyID, "_metadata.csv"))
    return(eSet)

}
```

返回的 eSet 是一个对象，需要大家仔细理解，才能进行后续分析。我在生信菜鸟团博客不止一次强调过这个：[[basicExpressionSet.md at master · bioconductor-chinabasic|eSet对象]]

## **先下载原始芯片数据，再自行处理**

原始芯片数据作者肯定上传到GEO啦，每个数据集的主页都可以看到各种链接，当然也可以不进入数据集的主页，自己凭空想象出下载链接，因为它们的链接都是有规律的，所以我写了函数来帮助大家获取下载链接，函数如下；

```
 get_GSE_links <- 
function(studyID = "GSE1009", down = F, destdir = "./") {
    ## studyID destdir ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE1nnn/GSE1009/matrix/GSE1009_series_matrix.txt.gz
    ## ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE1nnn/GSE1009/suppl/GSE1009_RAW.tar
    ## http://www.ncbi.nlm.nih.gov/geo/browse/?view=samples&mode=csv&series=1009

    supp_link = paste0("ftp://ftp.ncbi.nlm.nih.gov/geo/series/", substr(studyID, 1, nchar(studyID) - 3), "nnn/", 
        studyID, "/suppl/", studyID, "_RAW.tar")
    meta_link = paste0("http://www.ncbi.nlm.nih.gov/geo/browse/?view=samples&mode=csv&series=", substr(studyID, 
        4, nchar(studyID)))
    matrix_link = paste0("ftp://ftp.ncbi.nlm.nih.gov/geo/series/", substr(studyID, 1, nchar(studyID) - 3), "nnn/", 
        studyID, "/matrix/", studyID, "_series_matrix.txt.gz")

    print(paste0("The URL for raw data is : ", supp_link))
    print(paste0("The URL for metadata is : ", meta_link))
    print(paste0("The URL for matrix   is : ", matrix_link))

}
```

根据GEO的ID号，我的函数会自动判断跟它相关的3个链接，大家可以自己复制粘贴到浏览器去下载，也可以用R函数来下载。

```
> get_GSE_links("GSE42728")
[1] "The URL for raw data is : ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE42nnn/GSE42728/suppl/GSE42728_RAW.tar"
[1] "The URL for metadata is : http://www.ncbi.nlm.nih.gov/geo/browse/?view=samples&mode=csv&series=42728"
[1] "The URL for matrix   is : ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE42nnn/GSE42728/matrix/GSE42728_series_matrix.txt.gz"

download.file('ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE42nnn/GSE42872/suppl/GSE42872_RAW.tar',destfile = 'GSE42872_RAW.tar')
```

可以看到最后那个series\_matrix文件其实也是作者处理好的表达矩阵，不过我们需要理解的是如何处理原始芯片数据。

原始的芯片数据处理主要取决于芯片平台，下面我们就一一讲解：

### **旧版的affymetrix芯片**

用affy包，我曾经写过教程：用affy包读取affymetix的基因表达芯片数据-CEL格式数据

```
library(affy)
#perform mas5 normalization
affy_data = ReadAffy(celfile.path=dir_cels)
eset.mas5 = mas5(affy_data)
exprSet.nologs = exprs(eset.mas5)
exprSet = log(exprSet.nologs, 2)  #transform to Log_2 if needed

library(affy)
data <- ReadAffy(celfile.path=dir_cels) 
eset <- rma(data)
write.exprs(eset,file="data.txt")
```

下面是一些芯片平台的介绍：

img

### **新版的affymetrix芯片**

比如 Human Gene 1.0 St Array ，用oligo，我曾经写过教程：用oligo包来读取affymetix的基因表达芯片数据-CEL格式数据

```
library(oligo)
celFiles <- list.celfiles()
affyRaw <- read.celfiles(celFiles)
library(pd.mogene.2.0.st)  
## 根据芯片平台来载入芯片设计包，没办法自动选择，跟芯片探针包不一样：mogene20sttranscriptcluster.db
eset <- rma(affyRaw)
write.exprs(eset,file="data.txt")
```

上面是小鼠的芯片，下面是人类的芯片数据处理代码：

```
studyID='GSE42872';
studyID_probe=paste0(studyID,'_probe')
studyID_gene=paste0(studyID,'_gene')
R_history_data <- paste0(studyID,'.Rdata')
if ( file.exists(R_history_data)){
  load( R_history_data )
}else{
  library(oligo)
  ## the directory data should have raw CEL files 
  geneCELs=list.celfiles('data',listGzipped=T,full.name=T) 
  affyGeneFS <- read.celfiles(geneCELs)   
  geneCore <- rma(affyGeneFS, target = "core") 
  genePS <- rma(affyGeneFS, target = "probeset") 
  featureData(genePS) <- getNetAffx(genePS, "probeset")
  featureData(geneCore) <- getNetAffx(geneCore, "transcript")

}

exprSet=exprs( genePS )
pdata=pData( genePS )
```

下面是一些芯片平台的介绍：

img

### **更新的芯片版本**

比如HTA1.0或者HTA2.0，好处比拟转录组测序数据。它们其实有专门的界面版本的软件处理，相关R包目前还没有。

img

### **illumina相关芯片**

如果illumina的，我也在生信菜鸟团写过博客介绍： 用lumi包来处理illumina的bead系列表达芯片

```
rm(list=ls())
library(lumi)
# setwd('G:/array/illumina-beadseed-v4/lumi_example')
# fileName <- 'Barnes_gene_profile.txt' # Not Run
## 首先是从illumina的芯片结果文件，自己用R的lumi包来获取表达矩阵。
setwd('G:/array/illumina-beadseed-v4/GSE30669')
fileName <- 'GSE30669_HEK_Sample_Probe_Profile.txt' # Not Run
x.lumi <- lumiR.batch(fileName) ##, sampleInfoFile='sampleInfo.txt')
pData(phenoData(x.lumi))
## Do all the default preprocessing in one step
lumi.N.Q <- lumiExpresso(x.lumi)
### retrieve normalized data
dataMatrix <- exprs(lumi.N.Q)
## 下面是从GEO里面下载表达矩阵
rm(list=ls())
library(GEOquery)
library(limma)
GSE30669 <- getGEO('GSE30669', destdir=".",getGPL = F)
exprSet=exprs(GSE30669[[1]])
GSE30669[[1]]
pdata=pData(GSE30669[[1]])
exprSet=exprs(GSE30669[[1]])
## 很明显可以看到前面得到的dataMatrix 和后面得到的 exprSet 都是我们想要的表达矩阵
```

重点就是得到表达矩阵，它封装好了一个函数，lumiExpresso可以直接处理LumiBatch对象，这个函数结合了,N,T,B,Q(normalization,transformation,backgroud correction,qulity control)四个步骤，其中Q这个步骤又包括8种统计学图片。在该包的文章有详细说明：http://bioinformatics.oxfordjournals.org/content/24/13/1547.full

而 LumiBatch 对象是通过 lumiR.batch 读取的芯片文件被Illumina Bead Studio toolkit 处理的结果，也就是通常我们从公司或者GEO下载的数据( level 3 的 process data)。

### **其它数据芯片**

再比如agilent公司的， 已经各种各样的实验室定制化芯片，他们的原始芯片数据其实是没有现成的R包的，我们只能相信作者上传的表达矩阵是正确的，直接利用其表达矩阵做下游分析即可。

### **写在最后**

总之，我们要得到所有检测到的基因在所有样本的表达量信息， 就是我们通常说的表达矩阵，才能继续下游分析。

插个题外话，很多朋友会有整合不同的数据集的需求，这个时候需要额外注意批次效应的问题。可以用 RUVseq和svaseq 来找到全新的未知的的因素，再加上我们已知的因素，然后有了这些因素，就可以用 ComBat 和 removeBatchEffect 这样的工具来进行去除批次效应啦。

