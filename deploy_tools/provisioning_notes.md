Provisioning a new site
=======================
## Required packages:

* nignx
* Python 3
* Git
* Pip
* pyenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staning.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── env
