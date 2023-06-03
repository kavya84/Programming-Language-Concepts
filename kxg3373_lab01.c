//NAME : Kavya Sri Garikipati
//net id:kxg3373
//Student ID: 1001953373
//macOS Monterey version 12.5.1 
//writing program in C Language and executing in CMD via OMEGA
//execution steps in CMD
//compiling - [kxg3373@omega ~]$ gcc kxg3373_lab01.c
//execution - [kxg3373@omega ~]$ ./a.out

#include<stdio.h>
#include<string.h>
#include<dirent.h>
#include<sys/stat.h>

int main()
{
 int Total_fileSize = getDirectorySize(".");//Calculating the total size of the file
 printf("\n\nThe Total Size of the File is %d\n",Total_fileSize);//print the total size of the file
 return 0;
}

int getDirectorySize(char length[])
{
 int sum = 0;// Declaring total size 
 char directoryFiles[500]; // Declaring directory files as an array
 struct dirent *item;// dirent multiplied by item
 struct stat file;// this is used to check whether the path has file or directory
 DIR *directory = opendir(length);//this is known as directory stream for the directory path given
 while ((item=readdir(directory))!=NULL)
   {
    if(strcmp(item->d_name,".")==0 || strcmp(item->d_name,"..")==0)//"." is a hardlink to its containing directory.Therefore, it is skipped
      { // ".." indicates parent directory. Therefore it is skipped.
       continue;
      }
    strcpy(directoryFiles,length); //copy the string
    strcat(directoryFiles,"/");// concatenating the strings
    strcat(directoryFiles,item->d_name);// creates full path for items
    stat(directoryFiles,&file);// this is used to get information about the named file
    if(S_ISREG(file.st_mode))//this returns true if a file
      {
       FILE *filePointer = fopen(directoryFiles,"r");//this opens the files in reading mode
       fseek(filePointer,0L,SEEK_END);
       int res = ftell(filePointer);//ftell() is used to obtain the current value of the file position indicator for the file stream
       sum += res;// calculating sum in loop
       fclose(filePointer);
      }
      else
      {
       sum += getDirectorySize(directoryFiles);
      }
   }
  return sum;
}                                                                                                                                      








 










