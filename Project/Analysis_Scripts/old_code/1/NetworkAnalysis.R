library(igraph)

Data <- read.csv("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/FinalOutPutData/CompleteJSD.csv", header =FALSE)

#set working directory
setwd("/Users/jeffmills/PycharmProjects/EffiientKL_V1.0/D2LCStr_Results")

temp = list.files(pattern="*.csv")
MyData <- list()
for(i in 1:length(temp)){
  assign(temp[i], read.csv(temp[i], header = FALSE))
}
for(i in 1:length(temp)){
  MyData[i] <- read.csv(temp[i], header = FALSE)
}
View(MyData)

par(mfrow=c(6,6))
par(mar=c(1,1,1,1))

for (i in 1:32){
  L <- as.matrix(MyData[1])
  View(L)
  
  for(i in M){
    for(j in M[i]){
      j <- (j * (-1))
    }  
  }
  View(M)
  Nmst <- minimum.spanning.tree(M, algorithm = NULL)
  plot(Nmst, vertex.color = rainbow(52), vertex.size = 2, vertex.label = NA)
}
 


D <- as.matrix(Data)
G <- graph.adjacency(D,  weighted=TRUE, mode = "undirected")

Gmst <- minimum.spanning.tree(G, algorithm = "prim")

V(Gmst)$label <- V(Gmst)$name
V(Gmst)$shape <- "circle"
V(Gmst)$color <- "red"
V(Gmst)$size <- 4

V(Gmst)$degree <- degree(Gmst)

## Histogram of node degree
hist(V(Gmst)$degree,
        col = "red",
        main = "Histogram of MST Node Degree",
        ylab = "Freq",
        ylim = c(0, 200),
        xlab = "Degree of V" )

##Network Plot
set.seed(123)
plot(Gmst, vertex.label = NA)

##Highlight Degree & Layout
set.seed(123)
plot(Gmst, vertex.color = rainbow(52),
           vertex.size = V(Gmst)$degree,
           layout = layout.fruchterman.reingold,
           vertex.label = NA)

## Hub and Authorities
hs <- hub_score(Gmst)$vector
as <- authority.score(Gmst)$vector
par(mfrow=c(1,2))
set.seed(123)
plot(Gmst, vertex.size = hs*30,
           main = "Hubs",
           vertex.color = rainbow(52),
           vertex.label = NA)
           ##layout = layout.kamada.kawai)
set.seed(123)
plot(Gmst, vertex.size = as * 30,
     main = "Authorities",
     vertex.color = rainbow(52),
     vertex.label = NA)
     ##layout = layout.kamada.kawai)

##Community Detection

cnet <- cluster_edge_betweenness(Gmst)
set.seed(123)
plot(cnet,
     Gmst, 
     vertex.size = 1.5,
     vertex.label.cex = 0.8,
     vertex.label = NA
     )
dendPlot(cnet, mode= "hclust") 
View(Gmst)
str(cnet)
cnet[ 1:length(cnet) ]


