library(googlesheets4)
options(gargle_oauth_email = "sellis@ucsd.edu")


df <- read_sheet('1c7DZx09a5lljCDJp5DR9qf-Zt_whVCio-QL5pbPi_qk') %>% 
  filter(`Share publicly?` %in% c('Y',"Yes"))
quarter <- 'sp21'
# df$group <- unlist(df$Group)
setwd('/Users/shannonellis/Desktop/')

i = 1 

for(i in 2:nrow(df)){
  group <- df[i, 'group']
  file <- paste0('https://github.com/COGS108/group',group,'_', quarter,'.git')
  system(sprintf("git clone %s", file))
  direct <- paste0('group', group, '_', quarter, '/')
  notebook <- paste0('FinalProject_group',group,'.ipynb')
  path <- paste0(direct, notebook)
  if(file.exists(path)){
    system(sprintf('mv %s /Users/shannonellis/Desktop/Teaching/COGS108/FinalProjects-Sp21/', path))
    system(sprintf('rm -rf %s', direct))
  }else{
    print(paste0('file error in: group', group))
  }
  
}



### get all notebooks, not just publicly available

setwd('/Users/shannonellis/Desktop/')

#Fa19 https://github.com/COGS108/groupXXX 001-084 
#Wi20 https://github.com/COGS108/groupXXX_wi20 001-096
#Sp20 https://github.com/COGS108/groupXX_sp20 001-068; Note: there is no group 36
#Fa20 XXX_fa20 (001-071; No groups 009 or 049)

# quarter = 'wi20'
# 
# for(i in 1:96){
#   group <- str_pad(i, 3, pad = "0")
#   file <- paste0('https://github.com/COGS108/group',group, '_', quarter, '.git')
#   system(sprintf("git clone %s", file))
#   direct <- paste0('group',group,'_', quarter, '/')
#   notebook <- paste0('FinalProject_group',group,'.ipynb')
#   path <- paste0(direct, notebook)
#   if(file.exists(path)){
#     system(sprintf('mv %s /Users/shannonellis/Desktop/notebooks_analysis/all_notebooks/FinalProjects-Wi20/', path))
#     system(sprintf('rm -rf %s', direct))
#   }else{
#     print(paste0('file error in: group', group))
#   }
#   
# }


