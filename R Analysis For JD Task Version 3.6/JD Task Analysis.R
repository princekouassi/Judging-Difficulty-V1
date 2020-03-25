# Code to get some descriptive statistics from the JD experiment data file
#
#
#
# Last updated: 25/03/20
#
#
#
#

# Load libraries: 
library(plotly)
library(ggpubr)

# Load the data file ready for data sorting and filtering:
path = '~/Desktop/R Directory/R/JD Task Analysis/Pilot Data/p1.txt' # State data location
raw_data = read.csv(path, header =TRUE, sep = '', stringsAsFactors =FALSE) # Import data


#################################################################
#################################################################
#Get block order:
#################################################################
#################################################################
# Define function to determine the block order:
block_order = dget("order_blocks.R")
# Call the function to actually determine the block order to the raw data file:
expt_blocks = block_order(raw_data)
#################################################################
#################################################################



#################################################################
#################################################################
# Bootstrap CIs and means for gambles:
#################################################################
#################################################################
# Define function to boot strap CIs and means on gamble data:
strap_cis = dget("bootstrap_cis.R")
# Call the function to actually do CI and mean bootstrapping:
gamble_cis_upper = vector() # Store upper CIs
gamble_cis_lower = vector() # Store lower CIs
gamble_means = vector() # Store bootstrapped means
for(i in 1:6){  # Loop through the different blocks to get CIs and bootstrapped means
  block = expt_blocks[[i]] 
  data = block[6]
  data_vec = c(data[[1]])
  full_data = strap_cis(data_vec)
  gamble_means[i] = full_data[[3]]
  gamble_cis_lower[i] = full_data[[1]]
  gamble_cis_upper[i] = full_data[[2]]
}
# Add labels to the stored values:
names(gamble_means) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
names(gamble_cis_lower) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
names(gamble_cis_upper) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
#################################################################
#################################################################


#################################################################
#################################################################
# Bootstrap CIs and means for accuracy:
#################################################################
#################################################################
# Define function to boot strap CIs and means on accuracy data:
strap_cis_acc = dget("bootstrap_cis_acc.R")
# Call the function to actually do CI and mean bootstrapping:
acc_cis_upper = vector() # Store upper CIs
acc_cis_lower = vector() # Store lower CIs
acc_means = vector() # Store bootstrapped means
for(i in 1:6){  # Loop through the different blocks to get CIs and bootstrapped means
  block = expt_blocks[[i]] 
  data = block[2]
  data_vec = c(data[[1]])
  full_data = strap_cis_acc(data_vec,50)
  acc_means[i] = full_data[[3]]
  acc_cis_lower[i] = full_data[[1]]
  acc_cis_upper[i] = full_data[[2]]
}
# Add labels to the stored values:
names(acc_means) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
names(acc_cis_lower) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
names(acc_cis_upper) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
#################################################################
#################################################################


#################################################################
#################################################################
# Plot accuracy data:
#################################################################
#################################################################
# Data frame with accuracy for blue block:
Mean_Accuracy = acc_means[1:3] # Blue block
alci_b = acc_cis_lower[1:3] # Blue block
auci_b = acc_cis_upper[1:3] # Blue block
b_gamble_df = data.frame(
  Mean_Accuracy, # Mean accuracy
  alci_b, # Lower CIs 
  auci_b, # Upper CIs
  Block_Type = c("B1","B2","B3")
)
# Data frame with accuracy for orange block:
Mean_Accuracy_o = acc_means[4:6] # Blue block
alci_o = acc_cis_lower[4:6] # Blue block
auci_o = acc_cis_upper[4:6] # Blue block
o_gamble_df = data.frame(
  Mean_Accuracy_o, # Mean accuracy
  alci_o, # Lower CIs 
  auci_o, # Upper CIs
  Block_Type = c("B1","B2","B3")
)


# Define plot for blue block accuracy:
fig1 = ggplot(b_gamble_df, aes(Block_Type,Mean_Accuracy))+ # Define the plot area
  geom_point(data= b_gamble_df,size = 3, colour = 'blue')+ # Dot plot
  geom_errorbar(data = b_gamble_df, aes(Block_Type,Mean_Accuracy,ymin = alci_b , ymax = auci_b), width = 0.2, colour="black", size = 0.6)+ # Error bar plot
  labs(x = "Block Type", y = "Mean % Correct")+ # x and y asix lables AND title
  ylim(0.5, 1)+
  theme(
    panel.border = element_blank(), # Hide panel borders and remove grid lines
    panel.grid.major = element_blank(),
    panel.grid.minor.y = element_line(size=0.2,colour = "black", linetype = "dotted"),
    axis.line = element_line(colour = "black", size = 0.5), # Change axis line
    plot.background = element_rect(fill = "white"),
    panel.background = element_rect(fill = "lightgrey"), # Define panel background
    axis.title.x = element_blank(), # Define x axis
    axis.title.y = element_text(size = 10, face =2, vjust = -1), # Define y axis
    plot.title = element_text(size = 14, face = 2, hjust = 2),
    axis.text.x = element_text(face="bold", color="black", size=10,angle=45),
    axis.text.y = element_text(face="bold", color="black", size=10,angle=45)
  )

# Define plot for blue block accuracy:
fig2 = ggplot(o_gamble_df, aes(Block_Type,Mean_Accuracy_o))+ # Define the plot area
  geom_point(data= o_gamble_df,size = 3, colour = 'orange')+ # Dot plot
  geom_errorbar(data = o_gamble_df, aes(Block_Type,Mean_Accuracy_o,ymin = alci_o , ymax = auci_o), width = 0.2, colour="black", size = 0.6)+ # Error bar plot
  labs(x = "Block Type", y = "Percentage Correct")+ # x and y asix lables AND title
  ylim(0.5, 1)+
  theme(
    panel.border = element_blank(), # Hide panel borders and remove grid lines
    panel.grid.major = element_blank(),
    panel.grid.minor.y = element_line(size=0.2,colour = "black", linetype = "dotted"),
    axis.line = element_line(colour = "black", size = 0.5), # Change axis line
    plot.background = element_rect(fill = "white"),
    panel.background = element_rect(fill = "lightgrey"), # Define panel background
    axis.title.x = element_blank(), # Define x axis
    axis.title.y = element_blank(), # Define y axis
    plot.title = element_text(size = 14, face = 2, hjust = 2),
    axis.text.x = element_text(face="bold", color="black", size=10,angle=45),
      axis.text.y = element_text(face="bold", color="black", size=10,angle=45),
  ) 
#################################################################
#################################################################


#################################################################
#################################################################
# Plot gamble data:
#################################################################
#################################################################
# Data frame with gamble for blue block:
Mean_gamble = gamble_means[1:3] # Blue block
glci_b = gamble_cis_lower[1:3] # Blue block
guci_b = gamble_cis_upper[1:3] # Blue block
b_gam_df = data.frame(
  Mean_gamble, # Mean accuracy
  glci_b, # Lower CIs 
  guci_b, # Upper CIs
  Block_Type = c("B1","B2","B3")
)
# Data frame with accuracy for orange block:
Mean_gamble_o = gamble_means[4:6] # Blue block
glci_o = gamble_cis_lower[4:6] # Blue block
guci_o = gamble_cis_upper[4:6] # Blue block
o_gam_df = data.frame(
  Mean_gamble_o, # Mean accuracy
  glci_o, # Lower CIs 
  guci_o, # Upper CIs
  Block_Type = c("B1","B2","B3")
)


# Define plot for blue block gamble:
fig3 = ggplot(b_gam_df, mapping = aes(Block_Type,Mean_gamble))+ # Define the plot area
  geom_point(data= b_gam_df,size = 3, colour = 'blue')+ # Dot plot
  geom_errorbar(data = b_gam_df, aes(Block_Type,ymin = glci_b , ymax = guci_b), width = 0.2, colour="black", size = 0.6)+ # Error bar plot
  labs(x = "Block Type", y = "Mean Gamble")+ # x and y asix lables AND title
  ylim(30, 47)+
  theme(
    panel.border = element_blank(), # Hide panel borders and remove grid lines
    panel.grid.major = element_blank(),
    panel.grid.minor.y = element_line(size=0.2,colour = "black", linetype = "dotted"),
    axis.line = element_line(colour = "black", size = 0.5),# Change axis line
    plot.background = element_rect(fill = "white"),
    panel.background = element_rect(fill = "lightgrey"), # Define panel background
    axis.title.x = element_blank(), # Define x axis
    axis.title.y = element_text(size = 10, face =2, vjust = -1), # Define y axis
    plot.title = element_text(size = 14, face = 2, hjust = 2),
    axis.text.x = element_text(face="bold", color="black", size=10,angle=45),
    axis.text.y = element_text(face="bold", color="black", size=10,angle=45)
  )


# Define plot for orange block gamble:
fig4 = ggplot(o_gam_df, mapping = aes(Block_Type,Mean_gamble_o))+ # Define the plot area
  geom_point(data= o_gam_df,size = 3, colour = 'orange')+ # Dot plot
  geom_errorbar(data = o_gam_df, aes(Block_Type,ymin = glci_o , ymax = guci_o), width = 0.2, colour="black", size = 0.6)+ # Error bar plot
  labs(x = "Block Type", y = "Mean Gamble")+ # x and y asix lables AND title
  ylim(30, 47)+
  theme(
    panel.border = element_blank(), # Hide panel borders and remove grid lines
    panel.grid.major = element_blank(),
    panel.grid.minor.y = element_line(size=0.2,colour = "black", linetype = "dotted"),
    axis.line = element_line(colour = "black", size = 0.5),# Change axis line
    plot.background = element_rect(fill = "white"),
    panel.background = element_rect(fill = "lightgrey"), # Define panel background
    axis.title.x = element_blank(), # Define x axis
    axis.title.y = element_blank(), # Define y axis
    plot.title = element_text(size = 14, face = 2, hjust = 2),
    axis.text.x = element_text(face="bold", color="black", size=10,angle=45),
    axis.text.y = element_text(face="bold", color="black", size=10,angle=45)
  )
#################################################################
#################################################################


#################################################################
#################################################################
# Do plots as subplots:
#################################################################
#################################################################
# Create a subplot holder:
fig = ggarrange(fig1,fig2,fig3,fig4, 
          labels = c("A", "B","C","D"),
          ncol = 2, nrow = 2)
# Annotae the plots and call them:
annotate_figure(fig,
                bottom = text_grob("Block Type", color = "black", y = 1,x= 0.5, size =11, face = "bold"),
                top  = text_grob("Mean Accuracy and Gamble vs Block Type and Colour", color = "Black",size =12),
)
#################################################################
#################################################################

