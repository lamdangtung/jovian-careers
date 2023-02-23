# Database-Driven Web Applications

## Objective
- Connect a Flask web application to a cloud MySQL database
- Create dynamic pages by pulling information from database
- Add entries to the database using data from form submissions
- Deploy a production-ready database-driven web application

## Prerequisites
- Python
- Flask
- HTML
- CSS
- SQL

## Topics Covered
- Cloud Databases (PlanetScale)
- SQLAlchemy
- HTML lists & forms
- Dynamic Web Pages
- Spam Protection


## Important Links
- Starter project: https://github.com/aakashns/jovian-careers-website
- Finished code: https://github.com/aakashns/jovian-careers-website-v2
- Starter site: https://joviancareers.xyz
- Wireframes: https://app.excalidraw.com/s/2NiSy9956hc/8ihFsZTCbBo
- Sample Jobs Data: https://docs.google.com/spreadsheets/d/1-yHswQnVdwPcnvlJwUNkqZ2HvbsNkg1b5qIxaQLlNXk/edit?usp=sharing
- Finished site: https://joviancareers.com 
- MySQL Workbench: https://dev.mysql.com/downloads/workbench/
- SQLAlchemy Tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
- Email Sending API: https://mailjet.com
- HCaptcha Docs: https://www.hcaptcha.com/

## Step 1 - Set up project and cloud database
- Copy GitHub project, open on Replit, and deploy to Render
- Set up a cloud MySQL database on PlanetScale
- Create `jobs` table and add data using MySQL Workbench
- Connect to database from Replit using SQLAlchemy
### SQL Statement to Create `jobs` Table

```
CREATE TABLE jobs (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(120) NOT NULL,
  location VARCHAR(120) NOT NULL,
  salary INT,
  currency VARCHAR(10),
  responsibilities VARCHAR(2000),
  requirements VARCHAR(2000),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```

## Step 2 - Create database-driven dynamic pages
- Display list of jobs from cloud DB using SQL alchemy
- Create dynamic pages to display each job role
- Share layout, styles, and navigation using bootstrap
- Push updated code to GitHub and deploy to Render

## Step 3 - Store submitted applications in database
- Add a form to collect applications on job details page
- Create a flask route to handle application form submissions
- Create a table to store applications in cloud database
- Store submitted applications and show acknowledgement

### SQL Statement to Create `applications` Table

```
CREATE TABLE applications (
  id INT NOT NULL AUTO_INCREMENT,
  job_id INT NOT NULL,
  full_name VARCHAR(250) NOT NULL,
  email VARCHAR(250) NOT NULL,
  linkedin_url VARCHAR(500),
  education VARCHAR(2000),
  work_experience VARCHAR(2000),
  resume_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```

## Step 4 - Functional & Aesthetic Improvements
- Validate application form responses before submission 
- Send an email to admin and candidate on application submission
- Use a captcha in the application form to prevent spam/bots
- Provide an API to access individual job listings & applications by ID