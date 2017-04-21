# info6850-final-project
Proposal for Services For For TechnoFuture

## Overview
Margaret Vail is pleased to submit this proposal for services to support TechnoFuture digitally monitor the technology market to determine current and future trends.

## The Objective
- Keyword extraction and tracking
- Patent category tracking
- Complex patent identification

## The Solution (Demo)
- Online Dashboard written in Django
  * http://margaretvail.pythonanywhere.com/reports 
- Searchable and sortable data tables
  * http://margaretvail.pythonanywhere.com/reports/datatables/ 
- Display of individual patent information
  * http://margaretvail.pythonanywhere.com/reports/6505349/ 
- Admin interface to edit data
  * http://margaretvail.pythonanywhere.com/admin/ 
### Reports
- Keyword Tracking
  * http://margaretvail.pythonanywhere.com/reports/keywords/
- Patent Category Tacking
  * http://margaretvail.pythonanywhere.com/reports/categories/
- Complex Patent Identifications
  * Placeholder Page
### Charts
- http://margaretvail.pythonanywhere.com/reports/ 
### Git Version Control
- https://github.com/mvail/info6850-final-project 
### Code Highlights for TechnoFuture Engineers to review
- https://github.com/mvail/info6850-final-project/tree/master/ProcessData
- https://github.com/mvail/info6850-final-project/blob/master/mysite/reports/views.py
- https://github.com/mvail/info6850-final-project/tree/master/mysite/reports/templates/reports

## Demo Limitations
Following is a list of limitations in the current demo that will be fixed if the proposal is accepted:
- Data Tables Page is slow to load	
  * The data tables page is currently slow to load because it is loading every single patent, keyword and uspc before using jquery to transform it into a table. It is possible that the page will fail to load once, if this happens refresh the page and it should load the second time.
- USPC are not matched with their English Patent Category name	
  * The USPC is listed as a patent number. If this project is accepted, it will also display the English Patent Category name.
- Code Reusability
  * More functions can be created for reusable code.

## CONCLUSION
 
I look forward to working with TechnoFuture and supporting your efforts to improve your services. 
If you have questions on this proposal, feel free to contact Margaret Vail at your convenience by email at margaret@dal.ca. 

Thank you for your consideration,


Margaret Vail
