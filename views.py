from flask import render_template, request, redirect, url_for, session, escape
from app import app
from schedule_api import *
from calendarFunction import addToCalendar, clearCalendar
import urllib2
from html2text import html2text 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app.secret_key = 'Aasdfjsandkfnsfweorjo2348u9'

addedClasses = []

@app.route('/about')

def about(): 

	return render_template('about.html')



@app.route('/terms')
def index():
    
    options = {}
    options['terms'] = get_terms()
    if 'username' in session: 
    	options['UserName'] = escape(session['username'])

    return render_template('index.html', **options)


@app.route('/', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return render_template('login.html')

@app.route('/terms/term_code=<termCode>')
def termsCode(termCode):

	options = {}
	options['schools'] = get_schools(int(termCode))
	options['termCode'] = termCode

	return render_template('schools.html', **options)

@app.route('/terms/term_code=<termCode>/school=<schoolName>',methods=['GET', 'POST'])
def school(termCode, schoolName): 

	options = {} 
	other = {}
	value = True
	options['termCode'] = termCode
	options['schoolName'] = schoolName 
	options['subjects'] = get_subjects(int(termCode), schoolName)

	if request.method == 'POST':
	 	other['keyword'] = request.form['keyword']
	 	query = other['keyword'].split(' ')
	 	options['subjectName'] = query[0].upper()

	 	for i in options['subjects']:
			if i['SubjectCode'] == options['subjectName']:
	 			value = False
	 			break
	 	if (value):
	 		options['returnUrl'] = "/terms/term_code=" + termCode + "/school=" + schoolName
	 		return render_template('error.html', **options)

	# 	#check if only EECS
	 	if len(query) <= 1 or query[1] == '':
	 		options['subjects'] = ''
	 		options['catalogs'] = get_catalog_numbers(int(termCode), schoolName, options['subjectName'])
	 		return render_template('catalog.html', **options)

	 	options['catalogNumber'] = query[1]
	 	other['catalog'] = get_catalog_numbers(int(termCode),schoolName,options['subjectName'])
	 	value = True
	# 	#check if number is valid
	 	for i in other['catalog']:
	 		if i['CatalogNumber'] == int(options['catalogNumber']):
	 			value = False
	 			break
	 	if (value):
	 		options['subjects'] = ''
	 		options['catalogNumber'] = ''
	 		options['catalogs'] = get_catalog_numbers(int(termCode), schoolName, options['subjectName'])
	 		return render_template('catalog.html', **options)

	 	options['courseDescription'] = 'blank'
	 	options['courses'] = get_course_description(int(termCode), schoolName, options['subjectName'], int(options['catalogNumber']))
	 	options['sections'] = get_sections(int(termCode), schoolName, options['subjectName'], int(options['catalogNumber']))
		
	 	return render_template('courseInformation.html', **options)

	return render_template('subjects.html', **options)

@app.route('/terms/term_code=<termCode>/school=<schoolName>/subject=<subjectName>')
def catalog(termCode, schoolName, subjectName): 
	
	options ={} 
	options['termCode'] = termCode
	options['schoolName'] = schoolName 
	options['subjectName'] = subjectName 
	options['catalogs'] = get_catalog_numbers(int(termCode), schoolName, subjectName)


	return render_template('catalog.html', **options)

@app.route('/terms/term_code=<termCode>/school=<schoolName>/subject=<subjectName>/catalog_num=<catalogNumber>/course_descr=<courseDescription>/')
def courseInformation(termCode, schoolName, subjectName, catalogNumber, courseDescription): 

	
	try: 
		options ={} 
		options['termCode'] = termCode
		options['schoolName'] = schoolName 
		options['subjectName'] = subjectName 
		options['catalogNumber'] =catalogNumber
		options['courses'] = get_course_description(int(termCode), schoolName, subjectName, int(catalogNumber))
		options['sections'] = get_sections(int(termCode), schoolName, subjectName, int(catalogNumber))


		url = "https://www.koofers.com/university-of-michigan-ann-arbor-umich/" + subjectName + "/" + str(catalogNumber) + "-" + courseDescription + "/"

		AvgGPA = "N/A"

		try: 
			(html2text(urllib2.urlopen(url).read()).split("\n"))
		 	GPA = html2text(urllib2.urlopen(url).read()).split("\n")

		 	listLength = len(GPA)
		 	for x in range(0, listLength): 
		 		if GPA[x] == 'Avg GPA':
		 			AvgGPA = GPA[x+2][1:6]
		except: 
			pass


		options['Koofers'] = AvgGPA

		return render_template('courseInformation.html', **options)

	except:

		options ={} 
		options['termCode'] = termCode
		options['schoolName'] = schoolName 
		options['subjectName'] = subjectName
		options['returnUrl'] = "/terms/term_code=" + termCode + "/school=" + schoolName + "/subject=" + subjectName
		return render_template('error.html', **options)




@app.route('/terms/term_code=<termCode>/school=<schoolName>/subject=<subjectName>/catalog_num=<catalogNumber>/section_num=<sectionNumber>', methods = ['GET', 'POST'])
def sectionInfo(termCode, schoolName, subjectName, catalogNumber, sectionNumber):

	options = {}
	options['termCode'] = termCode
	options['schoolName'] = schoolName 
	options['subjectName'] = subjectName 
	options['catalogNumber'] =catalogNumber
	options['sectionNumber'] = sectionNumber
	options['sectionDetails'] = get_section_details(int(termCode), schoolName, subjectName, int(catalogNumber), str(sectionNumber))
	options['meetings'] = get_meetings(int(termCode), schoolName, subjectName, int(catalogNumber), str(sectionNumber))
	options['textbooks'] = get_textbooks(int(termCode), schoolName, subjectName, int(catalogNumber), str(sectionNumber))
	options['instructors'] = get_instructors(int(termCode), schoolName, subjectName, int(catalogNumber), str(sectionNumber))

	SectionDetails = get_section_details(int(termCode), schoolName, subjectName, int(catalogNumber), str(sectionNumber))
	



	try: 

		overallQuality = "N/A"
		averageGPA = "N/A"
		options['professorGPA'] = averageGPA
		options['professorQuality'] = overallQuality

		first = []
		last = []

		if "Instructor" in SectionDetails: 

			for teacher in SectionDetails['Instructor']:
				firstName = str(teacher['FirstName'])
				firstList = firstName.split()
				first.append(firstList[0])
				lastName = str(teacher['LastName'])
				lastList = lastName.split()
				last.append(lastList[0])


			searchUrl = "http://www.ratemyprofessors.com/search.jsp?query=University+of+Michigan+" + first[0] + '+' + last[0]

			rateProfessor = html2text(urllib2.urlopen(searchUrl).read()).split("\n")

			listLength = len(rateProfessor)

			Url = "" 
			searchString = firstName + " University of Michigan,"
			for x in range(0, listLength): 
				if searchString in rateProfessor[x]:
					Url = rateProfessor[x].split("(")[1][0:-1]

			newUrl = "http://www.ratemyprofessors.com" + Url 

			options['x'] = newUrl 


			ratedProfessorPage = html2text(urllib2.urlopen(newUrl).read()).split("\n")
			professorLength = len(ratedProfessorPage)
			for x in range(0, professorLength): 
				if ratedProfessorPage[x] == 'Overall Quality':
					overallQuality = ratedProfessorPage[x+2]
					options['professorQuality'] = overallQuality
				if ratedProfessorPage[x] == 'Average Grade': 
					averageGPA = ratedProfessorPage[x+2]
					options['professorGPA'] = averageGPA
	except: 
		pass 

	try: 

		overallQuality1 = "N/A"
		averageGPA1 = "N/A"
		options['professorGPA1'] = averageGPA
		options['professorQuality1'] = overallQuality

		if "Instructor" in SectionDetails: 
			firstName = str(SectionDetails['Instructor']['FirstName'])
			firstList = firstName.split()
			first = firstList[0]
			lastName = str(SectionDetails['Instructor']['LastName'])
			lastList = lastName.split()
			last = lastList[0]


			searchUrl = "http://www.ratemyprofessors.com/search.jsp?query=University+of+Michigan+" + first + '+' + last

			rateProfessor = html2text(urllib2.urlopen(searchUrl).read()).split("\n")

			listLength = len(rateProfessor)

			Url = "" 
			searchString = firstName + " University of Michigan,"
			for x in range(0, listLength): 
				if searchString in rateProfessor[x]:
					Url = rateProfessor[x].split("(")[1][0:-1]

			newUrl = "http://www.ratemyprofessors.com" + Url 

			options['x'] = newUrl 


			ratedProfessorPage = html2text(urllib2.urlopen(newUrl).read()).split("\n")
			professorLength = len(ratedProfessorPage)
			for x in range(0, professorLength): 
				if ratedProfessorPage[x] == 'Overall Quality':
					overallQuality1 = ratedProfessorPage[x+2]
					options['professorQuality1'] = overallQuality
				if ratedProfessorPage[x] == 'Average Grade': 
					averageGPA1 = ratedProfessorPage[x+2]
					options['professorGPA1'] = averageGPA
	except: 
		pass 


	options['p'] = "N/A"

	try: 
		nameList = []
		num = 0 
		p = []

		if "Instructor" in SectionDetails: 
			for teacher in SectionDetails['Instructor']:
				firstName = str(teacher['FirstName']).split()
				adjustedFirst = firstName[0]
				name = str(teacher['FirstName']) + ' ' + str(teacher['LastName'])
				name = name.replace(' ', '+')
				nameList.append(name)
				options['first'] = name
				fixed_name = '[' + adjustedFirst 
				quote = []
				newUrl = ''
				searchUrl = "http://umich.uloop.com/professors/?s=" + nameList[num] + "&verification=1"
				rateProfessor = html2text(urllib2.urlopen(searchUrl).read()).split("\n")
				listLength = len(rateProfessor)
				for x in range(0, listLength): 
					newString = rateProfessor[x].split()
					stringLength = len(newString)
					for y in range(0, stringLength): 
				 		if newString[y] == fixed_name:


				 			replaceString = '[' + str(teacher['FirstName']) + ' ' + str(teacher['LastName']) + '](/professors/'
				 			junk = rateProfessor[x].replace(replaceString, '')
				 			newUrl = "http://umich.uloop.com/professors/" + junk
				 			newUrl = str(newUrl[:-1])
				 			options['a'] = newUrl 
							professorUrl = html2text(urllib2.urlopen(newUrl).read()).split("\n")
							urlLength = len(professorUrl)
							b = 0
							for a in range(0, urlLength):
								b = b + 1 
								newWords = professorUrl[a].split()
								if len(newWords) == 3: 
									if newWords[0] == 'Rating': 
										if newWords[1] == '|': 
											if newWords[2] == 'Comment': 
												importantStuff = professorUrl[b+2:urlLength]
												options['f'] = importantStuff 
												stuffLength = len(importantStuff)
												for d in range(0, stuffLength): 
													if importantStuff[d] != '\n': 
														splitString = importantStuff[d].split()
														splitLength = len(splitString)
														if splitLength >= 1: 
															if splitString[0] == '|': 
																quote.append(importantStuff[d][3:])
																p.append(quote)
																options['p'] = quote
																num = num + 1


	except: 
		pass 

	options['q'] = "N/A"

	try: 
		if "Instructor" in SectionDetails: 
			firstName = str(SectionDetails['Instructor']['FirstName']).split()
			adjustedFirst = firstName[0]
			name = str(SectionDetails['Instructor']['FirstName']) + ' ' + str(SectionDetails['Instructor']['LastName'])
			name = name.replace(' ', '+')
			options['first'] = name
			fixed_name = '[' + adjustedFirst 



			quote = []
			newUrl = ''
			searchUrl = "http://umich.uloop.com/professors/?s=" + name + "&verification=1"
			rateProfessor = html2text(urllib2.urlopen(searchUrl).read()).split("\n")
			listLength = len(rateProfessor)
			for x in range(0, listLength): 
				newString = rateProfessor[x].split()
				stringLength = len(newString)
				for y in range(0, stringLength): 
			 		if newString[y] == fixed_name:
			 			replaceString = '[' + str(SectionDetails['Instructor']['FirstName']) + ' ' + str(SectionDetails['Instructor']['LastName']) + '](/professors/'
			 			junk = rateProfessor[x].replace(replaceString, '')
			 			newUrl = "http://umich.uloop.com/professors/" + junk
			 			newUrl = str(newUrl[:-1])
			 			options['a'] = newUrl 
						professorUrl = html2text(urllib2.urlopen(newUrl).read()).split("\n")
						urlLength = len(professorUrl)
						b = 0
						for a in range(0, urlLength):
							b = b + 1 
							newWords = professorUrl[a].split()
							if len(newWords) == 3: 
								if newWords[0] == 'Rating': 
									if newWords[1] == '|': 
										if newWords[2] == 'Comment': 
											importantStuff = professorUrl[b+2:urlLength]
											options['f'] = importantStuff 
											stuffLength = len(importantStuff)
											for d in range(0, stuffLength): 
												if importantStuff[d] != '\n': 
													splitString = importantStuff[d].split()
													splitLength = len(splitString)
													if splitLength >= 1: 
														if splitString[0] == '|': 
															quote.append(importantStuff[d][3:])
															options['q'] = quote


	except: 
		pass 

	try: 

		location = get_meetings(termCode,schoolName,subjectName,catalogNumber,sectionNumber)
		address = location[0]['Location']
		address = address.split()
		addressLength = len(address)
		newAbb = '' 
		newAddress = 'N/A'
		options['A'] = newAddress

		if addressLength >= 1:
			if address[0] == "AUD":
				if len(address[1]) == 1: 
					if addressLength == 3:
						newAbb = address[2]
					elif addressLength == 4:
						newAbb = address[3] + ' ' + address[4]
					elif addressLength == 5:
						newAbb = address[2] + ' ' + address[3] + ' ' + address[4]

					mapURL = html2text(urllib2.urlopen("http://www.ro.umich.edu/buildings.php").read()).split("\n")

					options['x'] = mapURL

					length = len(mapURL)

					newAddress = ''
					for i in range(0,length):
						newStringLength = len(mapURL[i])
						newAbbLength = len(newAbb)
						splittedString = mapURL[i].split() 
						splitLength = len(splittedString)
						if splitLength > 1: 

							if address[2] == splittedString[0]: 

								newAddress = mapURL[i][newAbbLength + 2: newStringLength + 1].split('|')
								newAddress = newAddress[0]

					options['A'] = newAddress
				else: 
					if addressLength == 2:
						newAbb = address[1]
					elif addressLength == 3:
						newAbb = address[1] + ' ' + address[2]
					elif addressLength == 4:
						newAbb = address[1] + ' ' + address[2] + ' ' + address[3]
					mapURL = html2text(urllib2.urlopen("http://www.ro.umich.edu/buildings.php").read()).split("\n")

					options['x'] = mapURL

					length = len(mapURL)
					newAddress = ''
					for i in range(0,length):
						newStringLength = len(mapURL[i])
						newAbbLength = len(newAbb)
						splittedString = mapURL[i].split() 
						splitLength = len(splittedString)
						if splitLength > 1: 

							if address[1] == splittedString[0]: 

								newAddress = mapURL[i][newAbbLength + 2: newStringLength + 1].split('|')
								newAddress = newAddress[0]

					options['A'] = newAddress

			else:
				if addressLength == 2:
					newAbb = address[1]
				elif addressLength == 3:
					newAbb = address[1] + ' ' + address[2]
				elif addressLength == 4:
					newAbb = address[1] + ' ' + address[2] + ' ' + address[3]

				mapURL = html2text(urllib2.urlopen("http://www.ro.umich.edu/buildings.php").read()).split("\n")

				options['x'] = mapURL

				length = len(mapURL)
				newAddress = ''
				for i in range(0,length):
					newStringLength = len(mapURL[i])
					newAbbLength = len(newAbb)
					splittedString = mapURL[i].split() 
					splitLength = len(splittedString)
					if splitLength > 1: 

						if address[1] == splittedString[0]: 

							newAddress = mapURL[i][newAbbLength + 2: newStringLength + 1].split('|')
							newAddress = newAddress[0]

				if newAbb == 'DANA':
					newAddress = "Dana Building"
				if newAbb == 'A&AB': 
					newAddress = 'School of Art and Design'

				options['A'] = newAddress
				options['B'] = newAbb



	except: 
		pass 


	return render_template('sectionInfo.html', **options)

@app.route('/terms/term_code=<termCode>/school=<schoolName>/subject=<subjectName>/catalog_num=<catalogNumber>/section_num=<sectionNumber>/addClass')
def addClass(termCode, schoolName, subjectName, catalogNumber, sectionNumber):


	options = {}
	options['termCode'] = termCode
	options['schoolName'] = schoolName 
	options['subjectName'] = subjectName 
	options['catalogNumber'] =catalogNumber
	options['sectionNumber'] = sectionNumber

	sectionDetails = get_section_details(int(termCode), schoolName, subjectName, int(catalogNumber), str(sectionNumber))

	addedCourse = subjectName + str(catalogNumber) + ' (' + sectionDetails['SectionType'] + ')' 

	if addedCourse not in addedClasses: 
		addedClasses.append(addedCourse)
		addToCalendar (addedCourse, sectionDetails['Meeting']['Times'], sectionDetails['Meeting']['Days'] )

	from calendarFunction import calendar
	session['Backpacked'] = addedClasses
	options['Backpacked']= session['Backpacked']
	session['calendar'] = calendar
	options['calendar'] = session['calendar'] 


	return render_template("newClass.html", **options)

@app.route('/clear_backpack')
def clearBackpack(): 
	session.pop('username', None)
	del addedClasses[:]
	clearCalendar()
	return render_template("clearbackpack.html")
