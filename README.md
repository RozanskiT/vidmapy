# VidmaPy - wrapper for Kurucz's ATLAS/SYNTHE codes

VidmaPy is a python module that enable user to use the power of ATLAS/SYNTHE codes with just few lines of python code.

## Key features
* Easy access to ATLAS and SYNTHE codes through Python

### Example code
```python
# Computation of ATLAS model
from vidmapy.kurucz.atlas import Atlas
from vidmapy.kurucz.parameters import Parameters

worker = Atlas()

model = worker.get_model(Parameters(12000., 4.0, 0.0, 2.0))
```

## Getting Started

### Prerequisites

* Python3
* Conda - usefull but not necessary

### Download

Two steps:
* Clone the repository or download it as the .zip file:
  - Clone by:
    ```
    git clone https://github.com/RozanskiT/vidmapy.git
    ```
  - Download zip from:
  [vidmapy-master.zip](https://github.com/RozanskiT/vidmapy/archive/master.zip)
* Download and untar direcotires with necessary atomic data in /vidmapy/kurucz/atomic_data/
  - Can be downloaded from : [atomc data](https://drive.google.com/drive/folders/1H-lFH69fyWvwWydgO8uBS3TIAdZ9hWdc?usp=sharing)
  
## Tutorial
TODO: fulfill

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Ewa Niemczura
