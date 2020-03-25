# Function to split file up by blocks:
#
# The input to the fuction is the raw data file.
#
#
#  Last updated: 20/03/20
#
#
#
#

order_blocks = function(raw_data){
  # If colour order is blue first:
  if (raw_data[1,7] == 1) {
    block_1_blue = raw_data[1:50,1:7]
    block_2_blue = raw_data[51:100,1:7]
    block_3_blue = raw_data[101:150,1:7]
    block_1_orange = raw_data[151:200,1:7]
    block_2_orange = raw_data[201:250,1:7]
    block_3_orange = raw_data[251:300,1:7]
    # Create list store data from the blocks:
    blocks_list = list(block_1_blue,block_2_blue,block_3_blue,block_1_orange,block_2_orange,block_3_orange)
    # Give the different list items names according to block:
    names(blocks_list) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
    return(blocks_list)
    # If colour order is orange first
  } else if (raw_data[1,7] == 2) {
    block_1_orange = raw_data[1:50,1:7]
    block_2_orange = raw_data[51:100,1:7]
    block_3_orange = raw_data[101:150,1:7]
    block_1_blue = raw_data[151:200,1:7]
    block_2_blue = raw_data[201:250,1:7]
    block_3_blue = raw_data[251:300,1:7]
    # Create list store data from the blocks:
    blocks_list = list(block_1_blue,block_2_blue,block_3_blue,block_1_orange,block_2_orange,block_3_orange)
    # Give the different list items names according to block:
    names(blocks_list) = c("block_1_blue","block_2_blue","block_3_blue","block_1_orange","block_2_orange","block_3_orange")
    return(blocks_list) # This list is the ouput for the function
  }
}