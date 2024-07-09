"""
python --version : To check the version of python
conda --version : To check the version of conda
conda list : To check the list of packages installed in the environment
conda install package_name : To install a package
conda update package_name : To update a package
conda remove package_name : To remove a package
conda create --name env_name : To create a new environment
conda activate env_name : To activate the environment
conda deactivate : To deactivate the environment
conda env list : To list all the environments
conda env remove --name env_name : To remove an environment
conda env export > environment.yml : To export the environment
conda env create -f environment.yml : To create an environment from the environment.yml file
conda env update -f environment.yml : To update an environment from the environment.yml file
conda env export --from-history > environment.yml : To export the environment from history
conda env export --no-builds > environment.yml : To export the environment without builds
conda env export --from-history --no-builds > environment.yml : To export the environment from history without builds

pip install package_name : To install a package
pip freeze : To check the list of packages installed in the environment
pip freeze > requirements.txt : To export the environment
pip install -r requirements.txt : To install the environment
pip uninstall package_name : To uninstall a package
pip install --upgrade package_name : To upgrade a package
pip install --upgrade pip : To upgrade pip

jupyter notebook : To start the jupyter notebook
jupyter notebook list : To list the running jupyter notebooks
jupyter notebook stop 8888 : To stop the jupyter notebook running on port 8888
jupyter notebook stop all : To stop all the running jupyter notebooks
jupyter kernelspec list : To list all the kernels
jupyter kernelspec uninstall kernel_name : To uninstall a kernel
jupyter kernelspec install /path/to/kernel : To install a kernel
jupyter kernelspec install --user /path/to/kernel : To install a kernel for the current user
jupyter kernelspec install --name kernel_name /path/to/kernel : To install a kernel with a name


git --version : To check the version of git
git init : To initialize a git repository
git clone repository_url : To clone a git repository
git status : To check the status of the repository
git add file_name : To add a file to the staging area
git add . : To add all the files to the staging area
git commit -m "commit message" : To commit the changes
git log : To check the commit history
git branch : To check the branches
git branch branch_name : To create a new branch
git checkout branch_name : To switch to a branch
git merge branch_name : To merge a branch
git push origin branch_name : To push changes to a branch
git pull origin branch_name : To pull changes from a branch
git remote -v : To check the remote repository
git remote add origin repository_url : To add a remote repository
git remote remove origin : To remove a remote repository
git push origin --delete branch_name : To delete a branch from the remote repository
git stash : To stash the changes
git stash list : To list the stashed changes
git stash apply : To apply the stashed changes
git stash drop : To drop the stashed changes
git stash clear : To clear all the stashed changes
git reset --hard commit_id : To reset to a commit
git reset --hard HEAD~1 : To reset to the previous commit
git reset --hard origin/master : To reset to the remote master branch
git reset --soft commit_id : To reset to a commit and keep the changes


docker --version : To check the version of docker
docker run image_name : To run a docker container
docker ps : To list the running containers
docker ps -a : To list all the containers
docker stop container_id : To stop a container
docker rm container_id : To remove a container
docker images : To list the images
docker rmi image_id : To remove an image
docker build -t image_name . : To build an image
docker run -it image_name : To run an image interactively
docker run -d image_name : To run an image in detached mode
docker exec -it container_id /bin/bash : To run a command in a running container
docker cp file container_id:/path : To copy a file to a container


kaggle --version : To check the version of kaggle
kaggle competitions list : To list the competitions
kaggle competitions download competition_name : To download the competition data
kaggle datasets list : To list the datasets
kaggle datasets download dataset_name : To download the dataset
kaggle kernels list : To list the kernels
kaggle kernels download kernel_name : To download the kernel
kaggle kernels output kernel_name : To download the output of a kernel
kaggle kernels push -p /path kernel_name : To push a kernel
kaggle kernels pull kernel_name : To pull a kernel
kaggle kernels output kernel_name : To download the output of a kernel
kaggle kernels status kernel_name : To check the status of a kernel
kaggle kernels output kernel_name : To download the output of a kernel
kaggle kernels output kernel_name -p /path : To download the output of a kernel to a specific path
kaggle kernels output kernel_name -m : To download the output of a kernel with metadata



"""