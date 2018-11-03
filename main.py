import handler as h
import recorder as r
import luis as l

def main():
	# start recording
	r.record()

	# request to MS STT
	data = h.handler()
	if 'DisplayText' in data.keys():
		result = data['DisplayText']
		print("You say:", result)
		print("Wait for LUIS...")

		command = l.get_command(result)
		print("Command:", command)


	else:
		print("I don't understand you.")
		print("Recived data: ", data)



if __name__ == '__main__':
	main()