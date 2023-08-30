import struct
import threading
import time

class Joycon:
	def __init__(self, path):
		self.gamepad = open(path, "rb")
		self.x = 0
		self.y = 0
		self.left = 0
		self.right = 0
		self.t = threading.Thread(target = self.loop)
		self.t.start()

	def loop(self):
		while True:
			input = self.gamepad.read(8)
			_, value, digital_analog, index = struct.unpack("<Ihbb", input)
			if(digital_analog == 2):
				if(index == 0):
					self.x = value
				elif(index == 1):
					self.y = value
				self.left = self.clamp(self.x - self.y)
				self.right = self.clamp(-self.x - self.y)
				#print(self.left, self.right, sep = ',')
	def get(self):
		return (str(self.left) + ',' + str(self.right))

	def clamp(self, n):
		return min(32767, max(-32768, n))


def main():
	joycon = Joycon("/dev/input/js0")
	while True:
		print(joycon.get())
		time.sleep(0.5)

if __name__ == '__main__':
	main()
