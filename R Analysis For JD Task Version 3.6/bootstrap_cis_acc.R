# Function to bootsrap CIs for accuracy
#
#
# Last updated: 23/03/2020
#
#
#
#
#
#
#
#

bootstrap_cis_acc = function(data,num_trials){
  
  # Edge correct:
  filt_data = data[(data == 0)] # Find if there any zero values in the data
  if (length(filt_data) > 0 ){
    real_data = data # If there is a zero continue with the same dataset
  } else {
    real_data = c(data,0) # If there is no zero add one to the data
  }
  
  
  
  # 
  n = 1000 # How many resampling iterations
  mean_list= vector() # Make an empty vector
  for (i in 1:n){
    data = sample(real_data,replace=T) # Get the mean for one interation
    correct_data = data[(data == 1)]
    per_correct = length(correct_data)/num_trials
    mean_list[[i]] = per_correct # Store the mean of the ith iteration
  }
  
  ci = quantile(mean_list,c(0.05,0.95)) # The actual confidence intervals
  MEAN = mean(mean_list) # Overall data mean
  cis = list(ci[1],ci[2],MEAN) # Creat list to store CIs and overall mean
  names(cis) = c("lower_ci","upper_ci","mean") # Give the output list better labels 
  return(cis)
}
