# baraza-webapp
Web app for baraza.
This will be built using Python's flask framework, and hosted on heroku.

The Baraza Web App will be a dynamic website where anyone can visit for more information on how the baraza system works. Information that will be found here will be:
> 1. Information on what baraza is, how it works.
> 2. Anyone can view information on reported cases. These cases will be pulled from the database, but user information will be withheld such that, viewers can only see reported cases and the status.
> 3. Admin will use this site to register chiefs.

## Running the site on your local machine(Ubuntu).
To set-up and run the site locally, clone the repository to your local environment.

You'll need to have flask installed on your machine. Install by running the command:
> pip install Flask

This command will set up Flask globally i.e your entire pc. I think this can be skipped especially if you won't be using Flask and will only need it for this project.
Go [here for more details](http://flask.pocoo.org/) on installing and setting up Flask and a virtual environment.

Once flask and your virtual environment are set up, open the project folder. Run 
> virtualenv venv

to set up a virtual environment inside the project. Once that is done, activate the virtual environment by running

> . venv/bin/activate

When your virtual environment is up and running, run
> pip install flask

to set up Flask in this virtual environment.
Once Flask is set up, navigate to baraza-web-app/baraza.
From here, run
> python baraza.py

That will run the baraza site at the given address! :)

This was built using Python 2.7.12


## Contributing

Thanks for your interest in contributing to Baraza! There are many ways to contribute to the baraza website/wed app. To get started, take a look at [CONTRIBUTING.md](CONTRIBUTING.md).

## Participation Guidelines

This project adheres to a [code of conduct](https://www.mozilla.org/en-US/about/governance/policies/participation/). By participating, you are expected to uphold this code. Please report unacceptable behavior to wobadha@gmail.com .
