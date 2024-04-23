import matplotlib.pyplot as plt
import networkx as nx
import math

#Using the networkx library to facilitate the weighted graph creation for our implementation
dis = 0
space = nx.Graph()

#Start node verteces
space.add_edge("start" , "1", dis = math.sqrt((394 - 331)**2 + (809 - 719)**2))
space.add_edge("start" , "2", dis = math.sqrt((393 - 331)**2 + (606 - 719)**2))
space.add_edge("start" , "3", dis = math.sqrt((360 - 331)**2 + (452 - 719)**2))
space.add_edge("start" , "4", dis = math.sqrt((323 - 331)**2 + (245 - 719)**2))

# Node 1 verteces
space.add_edge("1" , "2", dis = math.sqrt((393 - 394)**2 + (606 - 809)**2))
space.add_edge("1" , "3", dis = math.sqrt((360 - 394)**2 + (452 - 809)**2))
space.add_edge("1" , "4", dis = math.sqrt((323 - 394)**2 + (245 - 809)**2))
space.add_edge("1" , "11", dis = math.sqrt((1033 - 394)**2 + (811 - 809)**2))

# Node 2 verteces
space.add_edge("2" , "3", dis = math.sqrt((360 - 393)**2 + (452 - 606)**2))
space.add_edge("2" , "6", dis = math.sqrt((583 - 393)**2 + (506 - 606)**2))
space.add_edge("2" , "8", dis = math.sqrt((714 - 393)**2 + (241 - 606)**2))
space.add_edge("2" , "10", dis = math.sqrt((891 - 393)**2 + (520 - 606)**2))
space.add_edge("2" , "12", dis = math.sqrt((1035 - 393)**2 + (609 - 606)**2))

# Node 3 verteces

space.add_edge("3" , "4", dis = math.sqrt((323 - 360)**2 + (245 - 452)**2))
space.add_edge("3" , "6", dis = math.sqrt((583 - 360)**2 + (506 - 452)**2))

# Node 4 verteces

space.add_edge("4" , "5", dis = math.sqrt((556 - 323)**2 + (36 - 452)**2))

# Node 5 verteces

space.add_edge("5" , "7", dis = math.sqrt((704 - 556)**2 + (241 - 36)**2))
space.add_edge("5" , "9", dis = math.sqrt((798 - 556)**2 + (203 - 36)**2))
space.add_edge("5" , "14", dis = math.sqrt((907 - 556)**2 + (55 - 36)**2))
space.add_edge("5" , "18", dis = math.sqrt((1063 - 556)**2 + (36 - 36)**2))

# Node 6 verteces

space.add_edge("6" , "8", dis = math.sqrt((714 - 583)**2 + (522 - 506)**2))
space.add_edge("6" , "7", dis = math.sqrt((704 - 583)**2 + (241 - 506)**2))
space.add_edge("6" , "9", dis = math.sqrt((798 - 583)**2 + (203 - 506)**2))
space.add_edge("6" , "12", dis = math.sqrt((714 - 583)**2 + (522 - 506)**2))

# Node 7 verteces

space.add_edge("7" , "9", dis = math.sqrt((798 - 704)**2 + (203 - 241)**2))
space.add_edge("7" , "8", dis = math.sqrt((714 - 704)**2 + (522 - 241)**2))
space.add_edge("7" , "14", dis = math.sqrt((907 - 704)**2 + (55 - 241)**2))

# Node 8 verteces

space.add_edge("8" , "9", dis = math.sqrt((798 - 714)**2 + (203 - 522)**2))
space.add_edge("8" , "10", dis = math.sqrt((891 - 714)**2 + (520 - 522)**2))
space.add_edge("8" , "12", dis = math.sqrt((1035 - 714)**2 + (609 - 522)**2))

# Node 9 verteces

space.add_edge("9" , "10", dis = math.sqrt((891 - 798)**2 + (520 - 203)**2))
space.add_edge("9" , "12", dis = math.sqrt((1035 - 798)**2 + (609 - 203)**2))
space.add_edge("9" , "13", dis = math.sqrt((905 - 798)**2 + (310 - 203)**2))
space.add_edge("9" , "14", dis = math.sqrt((907 - 798)**2 + (55 - 203)**2))
space.add_edge("9" , "16", dis = math.sqrt((1128 - 798)**2 + (709 - 203)**2))

# Node 10 verteces

space.add_edge("10" , "12", dis = math.sqrt((1035 - 891)**2 + (609 - 520)**2))
space.add_edge("10" , "13", dis = math.sqrt((905 - 891)**2 + (310 - 520)**2))
space.add_edge("10" , "14", dis = math.sqrt((907 - 891)**2 + (55 - 520)**2))
space.add_edge("10" , "15", dis = math.sqrt((1064 - 891)**2 + (413 - 520)**2))
space.add_edge("10" , "17", dis = math.sqrt((1175 - 891)**2 + (152 - 520)**2))

# Node 11 verteces

space.add_edge("11" , "12", dis = math.sqrt((1035 - 891)**2 + (609 - 520)**2))
space.add_edge("11" , "16", dis = math.sqrt((1128 - 891)**2 + (709 - 520)**2))
space.add_edge("11" , "15", dis = math.sqrt((1064 - 891)**2 + (413 - 520)**2))
space.add_edge("11" , "22", dis = math.sqrt((1365 - 891)**2 + (747 - 520)**2))
space.add_edge("11" , "23", dis = math.sqrt((1365 - 891)**2 + (598 - 520)**2))
space.add_edge("11" , "24", dis = math.sqrt((1480 - 891)**2 + (478 - 520)**2))
space.add_edge("11" , "27", dis = math.sqrt((1511 - 891)**2 + (501 - 520)**2))

# Node 12 vertices

space.add_edge("12" , "13", dis = math.sqrt((905 - 1035)**2 + (310 - 609)**2))
space.add_edge("12" , "15", dis = math.sqrt((1064 - 1035)**2 + (413 - 609)**2))
space.add_edge("12" , "16", dis = math.sqrt((1128 - 1035)**2 + (709 - 609)**2))

# Node 13 vertices

space.add_edge("13" , "14", dis = math.sqrt((907 - 905)**2 + (55 - 310)**2))
space.add_edge("13" , "15", dis = math.sqrt((1064 - 905)**2 + (413 - 310)**2))
space.add_edge("13" , "16", dis = math.sqrt((1128 - 905)**2 + (709 - 310)**2))
space.add_edge("13" , "17", dis = math.sqrt((1175 - 905)**2 + (152 - 310)**2))
space.add_edge("13" , "19", dis = math.sqrt((1211 - 905)**2 + (478 - 310)**2))
space.add_edge("13" , "23", dis = math.sqrt((1365 - 905)**2 + (598 - 310)**2))

# Node 14 vertices

space.add_edge("14" , "18", dis = math.sqrt((1063 - 907)**2 + (36 - 55)**2))

# Node 15 vertices

space.add_edge("15" , "16", dis = math.sqrt((1128 - 1064)**2 + (709 - 413)**2))
space.add_edge("15" , "17", dis = math.sqrt((1175 - 1064)**2 + (152 - 413)**2))
space.add_edge("15" , "19", dis = math.sqrt((1211 - 1064)**2 + (478 - 413)**2))
space.add_edge("15" , "21", dis = math.sqrt((1261 - 1064)**2 + (580 - 413)**2))
space.add_edge("15" , "23", dis = math.sqrt((1365 - 1064)**2 + (747 - 413)**2))

# Node 16 vertices

space.add_edge("16" , "21", dis = math.sqrt((1261 - 1128)**2 + (580 - 709)**2))
space.add_edge("16" , "22", dis = math.sqrt((1365 - 1128)**2 + (747 - 709)**2))
space.add_edge("16" , "23", dis = math.sqrt((1365 - 1128)**2 + (598 - 709)**2))
space.add_edge("16" , "24", dis = math.sqrt((1480 - 1128)**2 + (478 - 709)**2))
space.add_edge("16" , "26", dis = math.sqrt((1493 - 1128)**2 + (819 - 709)**2))
space.add_edge("16" , "27", dis = math.sqrt((1511 - 1128)**2 + (501 - 709)**2))


# Node 17 vertices

space.add_edge("17" , "18", dis = math.sqrt((1063 - 1175)**2 + (36 - 152)**2))
space.add_edge("17" , "19", dis = math.sqrt((1211 - 1175)**2 + (478 - 152)**2))
space.add_edge("17" , "20", dis = math.sqrt((1212 - 1175)**2 + (60 - 152)**2))

# Node 18 vertices

space.add_edge("18" , "20", dis = math.sqrt((1212 - 1063)**2 + (60 - 36)**2))
space.add_edge("18" , "25", dis = math.sqrt((1479 - 1063)**2 + (60 - 36)**2))
space.add_edge("18" , "32", dis = math.sqrt((1614 - 1063)**2 + (51 - 36)**2))

# Node 19 vertices

space.add_edge("19" , "20", dis = math.sqrt((1212 - 1211)**2 + (60 - 478)**2))
space.add_edge("19" , "21", dis = math.sqrt((1261 - 1211)**2 + (580 - 478)**2))
space.add_edge("19" , "22", dis = math.sqrt((1365 - 1211)**2 + (747 - 478)**2))
space.add_edge("19" , "23", dis = math.sqrt((1365 - 1211)**2 + (598 - 478)**2))
space.add_edge("19" , "24", dis = math.sqrt((1480 - 1211)**2 + (478 - 478)**2))
space.add_edge("19" , "27", dis = math.sqrt((1511 - 1211)**2 + (501 - 478)**2))

# Node 20 vertices 

space.add_edge("20" , "25", dis = math.sqrt((1479 - 1211)**2 + (60 - 478)**2))
space.add_edge("20" , "32", dis = math.sqrt((1614 - 1211)**2 + (51 - 478)**2))

# Node 21 vertices

space.add_edge("21" , "22", dis = math.sqrt((1365 - 1261)**2 + (747 - 580)**2))
space.add_edge("21" , "23", dis = math.sqrt((1365 - 1261)**2 + (598 - 580)**2))
space.add_edge("21" , "24", dis = math.sqrt((1480 - 1261)**2 + (478 - 580)**2))
space.add_edge("21" , "27", dis = math.sqrt((1511 - 1261)**2 + (501 - 580)**2))

# Node 22 vertices

space.add_edge("22" , "23", dis = math.sqrt((1365 - 1365)**2 + (598 - 747)**2))
space.add_edge("22" , "26", dis = math.sqrt((1493 - 1365)**2 + (819 - 747)**2))

# Node 23 vertices

space.add_edge("23" , "24", dis = math.sqrt((1480 - 1365)**2 + (478 - 598)**2))
space.add_edge("23" , "27", dis = math.sqrt((1511 - 1365)**2 + (501 - 598)**2))

# Node 24 vertices

space.add_edge("24" , "25", dis = math.sqrt((1479 - 1480)**2 + (60 - 478)**2))
space.add_edge("24" , "26", dis = math.sqrt((1493 - 1480)**2 + (819 - 478)**2))
space.add_edge("24" , "27", dis = math.sqrt((1511 - 1480)**2 + (501 - 478)**2))
space.add_edge("24" , "28", dis = math.sqrt((1516 - 1480)**2 + (112 - 478)**2))
space.add_edge("24" , "31", dis = math.sqrt((1651 - 1480)**2 + (478 - 478)**2))

# Node 25 vertices

space.add_edge("25" , "27", dis = math.sqrt((1511 - 1479)**2 + (501 - 60)**2))
space.add_edge("25" , "28", dis = math.sqrt((1516 - 1479)**2 + (112 - 60)**2))
space.add_edge("25" , "30", dis = math.sqrt((1622 - 1479)**2 + (596 - 60)**2))
space.add_edge("25" , "31", dis = math.sqrt((1651 - 1479)**2 + (526 - 60)**2))
space.add_edge("25" , "32", dis = math.sqrt((1614 - 1479)**2 + (51 - 60)**2))

# Node 26 vertices

space.add_edge("26" , "29", dis = math.sqrt((1622 - 1493)**2 + (757 - 819)**2))

# Node 27 vertices 

space.add_edge("27" , "28", dis = math.sqrt((1516 - 1511)**2 + (112 - 501)**2))
space.add_edge("27" , "30", dis = math.sqrt((1622 - 1511)**2 + (596 - 501)**2))
space.add_edge("27" , "31", dis = math.sqrt((1651 - 1511)**2 + (526 - 501)**2))

# Node 28 vertices

space.add_edge("28" , "30", dis = math.sqrt((1622 - 1516)**2 + (596 - 112)**2))
space.add_edge("28" , "31", dis = math.sqrt((1651 - 1516)**2 + (526 - 112)**2))
space.add_edge("28" , "32", dis = math.sqrt((1614 - 1516)**2 + (51 - 112)**2))

# Node 29 vertices

space.add_edge("29" , "30", dis = math.sqrt((1622 - 1622)**2 + (596 - 757)**2))
space.add_edge("29" , "31", dis = math.sqrt((1651 - 1622)**2 + (526 - 757)**2))
space.add_edge("29" , "Goal", dis = math.sqrt((1725 - 1622)**2 + (65 - 757)**2))

# Node 30 vertices

space.add_edge("30" , "31", dis = math.sqrt((1651 - 1622)**2 + (526 - 596)**2))

# Node 31 vertices

space.add_edge("31" , "33", dis = math.sqrt((1689 - 1651)**2 + (131 - 526)**2))
space.add_edge("31" , "Goal", dis = math.sqrt((1725 - 1651)**2 + (65 - 526)**2))

# Node 32 vertices

space.add_edge("32" , "33", dis = math.sqrt((1689 - 1614)**2 + (131 - 51)**2))
space.add_edge("32" , "Goal", dis = math.sqrt((1725 - 1614)**2 + (65 - 51)**2))

# Node 33 vertices

space.add_edge("33" , "Goal", dis = math.sqrt((1725 - 1689)**2 + (65 - 131)**2))


elarge = [(u, v) for (u, v, d) in space.edges(data=True) if d["dis"] > 500]
esmall = [(u, v) for (u, v, d) in space.edges(data=True) if d["dis"] <= 500]

pos = nx.spring_layout(space, seed=15)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(space, pos, node_size=700)

# node labels
nx.draw_networkx_labels(space, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(space, "dis")
nx.draw_networkx_edge_labels(space, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()