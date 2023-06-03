//NAME : Kavya Sri Garikipati
//Net id:kxg3373
//Student ID: 1001953373
//macOS Monterey version 12.5.1
//writing program in Java Language and executing in CMD with the help of OMEGA
//execution steps in CMD
//compiling - [kxg3373@omega ~]$ javac kxg3373_lab01.c
//execution - [kxg3373@omega ~]$ ./a.out

import java.io.File; //import java.io.file package

class kxg3373_lab01 //class
{
  public static void main(String[] args)//Main function declaration
   {
     String currentDirectory = System.getProperty("user.dir");//The directory where the program got launched
     File directory = new File(currentDirectory);// the file directory is created
     int Total_fileSize = getDirectorySize(directory);//directory size
     System.out.println(Total_fileSize);//The total file size is getting printed
   }
  static int getDirectorySize(File path)
  {
    int sum  = 0;// initializing sum to 0
    File[] directoryFiles = path.listFiles();//listing files within directory
    int dir_file_size = directoryFiles.length;//finding length of directory files

    for (int m = 0; m <dir_file_size ; m++) //iterating directory files
    {
      if (directoryFiles[m].isFile())
      {
        sum += directoryFiles[m].length();// the length of files is calculated here
      }
      else
      {
        sum += getDirectorySize(directoryFiles[m]);// calculate files
      }
    }
    return sum;// returns sum
  }
}
