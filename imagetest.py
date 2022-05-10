from PIL import Image
from ComputerVisionAlgorithms import ComputerVisionAlgorithms

path = "histReq.png"


ComputerVisionAlgorithms.histogram_equalization(
    Image.open(path), 100, 500, 100, 500).show()
