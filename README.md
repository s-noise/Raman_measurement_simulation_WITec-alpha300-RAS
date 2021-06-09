# Raman_measurement_simulation_WITec-alpha300-RAS
A python script for training and education purpose simulating an Raman measurement (session) on a graphene flake on a WITec alpha300 RAS device.
All the software related steps (from starting of the software, finding the sample position, alignment of the Raman signal, acquiring point spectra at sample positions with different layer numbers, till saving the data) are performed for a graphene flake with differnet layer numbers.

This small program can be used for training or education purpose, e.g. in the context of an online practical class.
Therefore, no initial guidance is given in the program itself and no "back" button is added for the individual steps during the simulated session.
The individual steps of the simulation, ~"slide by slide" are listed in the *Raman_sim_instructions.txt* file, visible after unzip of the *images.zip* directory.

Compatible with Windows, Linux and MAC operating systems

The program contains screenshots of licensed software. The screenshots and the instruction file for individual measurement steps *Raman_sim_instructions.txt* are password protected. Please send me a password request by e-mail to obtain the password which is needed to run the program: [stefan.noisternig@univie.ac.at](mailto:stefan.noisternig@univie.ac.at).

For guidance and more information on other measuring modes please also consider the official WITec Suite Help with included operation guides to each measuring mode (since WITec Suite 5.3).


## Installation:
an example is given for Linux Systems

* download files: *Raman_sim_v1.py*, *images.zip* and *images.z01* in a directory

* combine zip archives *images.zip* & *images.z01* into new zip archive:
  - go to the directory with the files and open terminal:
    ```bash
     zip -F images.zip --out images_new.zip
     ```
             
* request password for zip archive:
  [stefan.noisternig@univie.ac.at](mailto:stefan.noisternig@univie.ac.at)
            
* extract the zip archive:
  ```bash
  unzip images_new.zip 
  ```
## run:
* the *images* folder and *Raman_sim_v1.py* must be in the same directory
* go to the directory and execute *Raman_sim_v1.py* in python 3
  - e.g. in Linux:
    ```bash
    python Raman_sim_v1.py
    ```
## License
The License is given for the python file *Raman_sim_v1.py* itself and does not inlcude the content in the compressed *images* folders.

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
