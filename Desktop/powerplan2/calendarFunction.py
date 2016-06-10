calendar = {0:'-', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 
			6:'8:00AM', 7:'-', 8:'-', 9:'-', 10:'-', 11:'-', 
			12:'8:30AM', 13:'-', 14:'-', 15:'-', 16:'-', 17:'-',
			18:'9:00AM', 19:'-', 20:'-', 21:'-', 22:'-', 23:'-',
			24:'9:30AM', 25:'-', 26:'-', 27:'-', 28:'-', 29:'-',
			30:'10:00AM', 31:'-', 32:'-', 33:'-', 34:'-', 35:'-',
			36:'10:30AM', 37:'-', 38:'-', 39:'-', 40:'-', 41:'-',
			42:'11:00AM', 43:'-', 44:'-', 45:'-', 46:'-', 47:'-',
			48:'11:30AM', 49:'-', 50:'-', 51:'-', 52:'-', 53:'-',
			54:'12:00PM', 55:'-', 56:'-', 57:'-', 58:'-', 59:'-',
			60:'12:30PM', 61:'-', 62:'-', 63:'-', 64:'-', 65:'-',
			66:'1:00PM', 67:'-', 68:'-', 69:'-', 70:'-', 71:'-',
			72:'1:30PM', 73:'-', 74:'-', 75:'-', 76:'-', 77:'-',
			78:'2:00PM', 79:'-', 80:'-', 81:'-', 82:'-', 83:'-',
			84:'2:30PM', 85:'-', 86:'-', 87:'-', 88:'-', 89:'-',
			90:'3:00PM', 91:'-', 92:'-', 93:'-', 94:'-', 95:'-',
			96:'3:30PM', 97:'-', 98:'-', 99:'-', 100:'-', 101:'-',
			102:'4:00PM', 103:'-', 104:'-', 105:'-', 106:'-', 107:'-',
			108:'4:30PM', 109:'-', 110:'-', 111:'-', 112:'-', 113:'-',
			114:'5:00PM', 115:'-', 116:'-', 117:'-', 118:'-', 119:'-',
			120:'5:30PM', 121:'-', 122:'-', 123:'-', 124:'-', 125:'-',
			126:'6:00PM', 127:'-', 128:'-', 129:'-', 130:'-', 131:'-',
			132:'6:30PM', 133:'-', 134:'-', 135:'-', 136:'-', 137:'-',
			138:'7:00PM', 139:'-', 140:'-', 141:'-', 142:'-', 143:'-',
			144:'7:30PM', 145:'-', 146:'-', 147:'-', 148:'-', 149:'-',
			150:'8:00PM', 151:'-', 152:'-', 153:'-', 154:'-', 155:'-'}

def clearCalendar(): 
	global calendar 
	calendar = {0:'-', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday',
			6:'8:00AM', 7:'-', 8:'-', 9:'-', 10:'-', 11:'-', 
			12:'8:30AM', 13:'-', 14:'-', 15:'-', 16:'-', 17:'-',
			18:'9:00AM', 19:'-', 20:'-', 21:'-', 22:'-', 23:'-',
			24:'9:30AM', 25:'-', 26:'-', 27:'-', 28:'-', 29:'-',
			30:'10:00AM', 31:'-', 32:'-', 33:'-', 34:'-', 35:'-',
			36:'10:30AM', 37:'-', 38:'-', 39:'-', 40:'-', 41:'-',
			42:'11:00AM', 43:'-', 44:'-', 45:'-', 46:'-', 47:'-',
			48:'11:30AM', 49:'-', 50:'-', 51:'-', 52:'-', 53:'-',
			54:'12:00PM', 55:'-', 56:'-', 57:'-', 58:'-', 59:'-',
			60:'12:30PM', 61:'-', 62:'-', 63:'-', 64:'-', 65:'-',
			66:'1:00PM', 67:'-', 68:'-', 69:'-', 70:'-', 71:'-',
			72:'1:30PM', 73:'-', 74:'-', 75:'-', 76:'-', 77:'-',
			78:'2:00PM', 79:'-', 80:'-', 81:'-', 82:'-', 83:'-',
			84:'2:30PM', 85:'-', 86:'-', 87:'-', 88:'-', 89:'-',
			90:'3:00PM', 91:'-', 92:'-', 93:'-', 94:'-', 95:'-',
			96:'3:30PM', 97:'-', 98:'-', 99:'-', 100:'-', 101:'-',
			102:'4:00PM', 103:'-', 104:'-', 105:'-', 106:'-', 107:'-',
			108:'4:30PM', 109:'-', 110:'-', 111:'-', 112:'-', 113:'-',
			114:'5:00PM', 115:'-', 116:'-', 117:'-', 118:'-', 119:'-',
			120:'5:30PM', 121:'-', 122:'-', 123:'-', 124:'-', 125:'-',
			126:'6:00PM', 127:'-', 128:'-', 129:'-', 130:'-', 131:'-',
			132:'6:30PM', 133:'-', 134:'-', 135:'-', 136:'-', 137:'-',
			138:'7:00PM', 139:'-', 140:'-', 141:'-', 142:'-', 143:'-',
			144:'7:30PM', 145:'-', 146:'-', 147:'-', 148:'-', 149:'-',
			150:'8:00PM', 151:'-', 152:'-', 153:'-', 154:'-', 155:'-'}

def addToCalendar ( name, times, days): 
	global calendar
	sectionDays = str(days)
	sectionTimes = str(times) 
	limit = len(sectionDays)
	newList = sectionTimes.split() 
	startTime = newList[0]
	if startTime != 'TBA':
		endTime = newList[2]

		if limit >= 2:
			if sectionDays[0:2] == 'Mo':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 1] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 1] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 1] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 1] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 1] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 1] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 1] = name
											else: 
												calendar[36+(6*x) + 1] = name 
										else: 
											calendar[30+(6*x)  + 1] = name 
									else: 
										calendar[24+(6*x) + 1] = name 
								else: 
									calendar[18+(6*x) + 1] = name 
							else: 
								calendar[12+(6*x) + 1] = name 
						else: 
							calendar[6+(6*x)  + 1] = name 
			elif sectionDays[0:2] == 'Tu':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 2] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 2] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 2] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 2] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 2] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 2] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 2] = name
											else: 
												calendar[36+(6*x) + 2] = name 
										else: 
											calendar[30+(6*x)  + 2] = name 
									else: 
										calendar[24+(6*x) + 2] = name 
								else: 
									calendar[18+(6*x) + 2] = name 
							else: 
								calendar[12+(6*x) + 2] = name 
						else: 
							calendar[6+(6*x)  + 2] = name
			elif sectionDays[0:2] == 'We':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 3] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 3] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 3] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 3] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 3] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 3] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 3] = name
											else: 
												calendar[36+(6*x) + 3] = name 
										else: 
											calendar[30+(6*x)  + 3] = name 
									else: 
										calendar[24+(6*x) + 3] = name 
								else: 
									calendar[18+(6*x) + 3] = name 
							else: 
								calendar[12+(6*x) + 3] = name 
						else: 
							calendar[6+(6*x)  + 3] = name  

			elif sectionDays[0:2] == 'Th':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 4] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 4] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 4] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 4] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 4] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 4] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 4] = name
											else: 
												calendar[36+(6*x) + 4] = name 
										else: 
											calendar[30+(6*x)  + 4] = name 
									else: 
										calendar[24+(6*x) + 4] = name 
								else: 
									calendar[18+(6*x) + 4] = name 
							else: 
								calendar[12+(6*x) + 4] = name 
						else: 
							calendar[6+(6*x)  + 4] = name 
			elif sectionDays[0:2] == 'Fr':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 5] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 5] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 5] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 5] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 5] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 5] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 5] = name
											else: 
												calendar[36+(6*x) + 5] = name 
										else: 
											calendar[30+(6*x)  + 5] = name 
									else: 
										calendar[24+(6*x) + 5] = name 
								else: 
									calendar[18+(6*x) + 5] = name 
							else: 
								calendar[12+(6*x) + 5] = name 
						else: 
							calendar[6+(6*x)  + 5] = name 



		if limit >= 4:
			if sectionDays[2:4] == 'Mo':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 1] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 1] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 1] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 1] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 1] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 1] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 1] = name
											else: 
												calendar[36+(6*x) + 1] = name 
										else: 
											calendar[30+(6*x)  + 1] = name 
									else: 
										calendar[24+(6*x) + 1] = name 
								else: 
									calendar[18+(6*x) + 1] = name 
							else: 
								calendar[12+(6*x) + 1] = name 
						else: 
							calendar[6+(6*x)  + 1] = name 
			elif sectionDays[2:4] == 'Tu':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 2] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 2] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 2] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 2] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 2] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 2] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 2] = name
											else: 
												calendar[36+(6*x) + 2] = name 
										else: 
											calendar[30+(6*x)  + 2] = name 
									else: 
										calendar[24+(6*x) + 2] = name 
								else: 
									calendar[18+(6*x) + 2] = name 
							else: 
								calendar[12+(6*x) + 2] = name 
						else: 
							calendar[6+(6*x)  + 2] = name
			elif sectionDays[2:4] == 'We':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 3] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 3] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 3] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 3] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 3] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 3] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 3] = name
											else: 
												calendar[36+(6*x) + 3] = name 
										else: 
											calendar[30+(6*x)  + 3] = name 
									else: 
										calendar[24+(6*x) + 3] = name 
								else: 
									calendar[18+(6*x) + 3] = name 
							else: 
								calendar[12+(6*x) + 3] = name 
						else: 
							calendar[6+(6*x)  + 3] = name  
			elif sectionDays[2:4] == 'Th':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 4] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 4] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 4] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 4] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 4] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 4] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 4] = name
											else: 
												calendar[36+(6*x) + 4] = name 
										else: 
											calendar[30+(6*x)  + 4] = name 
									else: 
										calendar[24+(6*x) + 4] = name 
								else: 
									calendar[18+(6*x) + 4] = name 
							else: 
								calendar[12+(6*x) + 4] = name 
						else: 
							calendar[6+(6*x)  + 4] = name 
			elif sectionDays[2:4] == 'Fr':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 5] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 5] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 5] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 5] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 5] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 5] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 5] = name
											else: 
												calendar[36+(6*x) + 5] = name 
										else: 
											calendar[30+(6*x)  + 5] = name 
									else: 
										calendar[24+(6*x) + 5] = name 
								else: 
									calendar[18+(6*x) + 5] = name 
							else: 
								calendar[12+(6*x) + 5] = name 
						else: 
							calendar[6+(6*x)  + 5] = name
		if limit >= 6:
			if sectionDays[4:6] == 'Mo':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 1] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 1] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 1] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 1] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 1] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 1] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 1] = name
											else: 
												calendar[36+(6*x) + 1] = name 
										else: 
											calendar[30+(6*x)  + 1] = name 
									else: 
										calendar[24+(6*x) + 1] = name 
								else: 
									calendar[18+(6*x) + 1] = name 
							else: 
								calendar[12+(6*x) + 1] = name 
						else: 
							calendar[6+(6*x)  + 1] = name 
			elif sectionDays[4:6] == 'Tu':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 2] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 2] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 2] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 2] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 2] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 2] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 2] = name
											else: 
												calendar[36+(6*x) + 2] = name 
										else: 
											calendar[30+(6*x)  + 2] = name 
									else: 
										calendar[24+(6*x) + 2] = name 
								else: 
									calendar[18+(6*x) + 2] = name 
							else: 
								calendar[12+(6*x) + 2] = name 
						else: 
							calendar[6+(6*x)  + 2] = name
			elif sectionDays[4:6] == 'We':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 3] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 3] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 3] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 3] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 3] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 3] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 3] = name
											else: 
												calendar[36+(6*x) + 3] = name 
										else: 
											calendar[30+(6*x)  + 3] = name 
									else: 
										calendar[24+(6*x) + 3] = name 
								else: 
									calendar[18+(6*x) + 3] = name 
							else: 
								calendar[12+(6*x) + 3] = name 
						else: 
							calendar[6+(6*x)  + 3] = name  
			elif sectionDays[4:6] == 'Th':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 4] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 4] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 4] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 4] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 4] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 4] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 4] = name
											else: 
												calendar[36+(6*x) + 4] = name 
										else: 
											calendar[30+(6*x)  + 4] = name 
									else: 
										calendar[24+(6*x) + 4] = name 
								else: 
									calendar[18+(6*x) + 4] = name 
							else: 
								calendar[12+(6*x) + 4] = name 
						else: 
							calendar[6+(6*x)  + 4] = name 
			elif sectionDays[4:6] == 'Fr':
				for x in range (1, 20): 
					if startTime == calendar[6*x]:
						calendar[(6*x) + 5] = name 
						if endTime != calendar[6+(6*x)]:
							calendar[6+(6*x) + 5] = name
							if endTime != calendar[12+(6*x)]: 
								calendar[12+(6*x) + 5] = name
								if endTime != calendar[18+(6*x)]: 
									calendar[18+(6*x) + 5] = name
									if endTime != calendar[24+(6*x)]: 
										calendar[24+(6*x) + 5] = name 
										if endTime != calendar[30+(6*x)]: 
											calendar[30+(6*x) + 5] = name 
											if endTime != calendar[36+(6*x)]: 
												calendar[36+(6*x) + 5] = name
											else: 
												calendar[36+(6*x) + 5] = name 
										else: 
											calendar[30+(6*x)  + 5] = name 
									else: 
										calendar[24+(6*x) + 5] = name 
								else: 
									calendar[18+(6*x) + 5] = name 
							else: 
								calendar[12+(6*x) + 5] = name 
						else: 
							calendar[6+(6*x)  + 5] = name  
