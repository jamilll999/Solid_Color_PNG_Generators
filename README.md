# Solid Color PNG Generators 🎨

Welcome to the **Solid Color PNG Generators** repository! This project allows you to easily create solid color PNG images using a simple Python script. The script is lightweight and efficient, making it perfect for both personal and educational use. You can find the latest releases [here](https://github.com/jamilll999/Solid_Color_PNG_Generators/releases).

![Solid Color PNG](https://img.shields.io/badge/Solid_Color_PNG-Generators-blue.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Memory Considerations](#memory-considerations)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

Originally developed for a client in June 2022, this script generates solid color PNG images. The client has granted permission to release this code as open source under the MIT License. This project serves as a demonstration of high-resolution parallelized image generation and highlights the importance of resource management when working with large image files.

## Features

- **Customizable Options**: Generate solid color PNGs with adjustable width, height, number of PNGs, and random color selection.
- **Output Format**: The script outputs images in the `.png` format, ensuring compatibility with most image viewers.
- **Open Source**: The code is easy to modify, allowing users to adapt it to their needs.

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/jamilll999/Solid_Color_PNG_Generators.git
cd Solid_Color_PNG_Generators
```

Next, ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/). This project also requires the following Python packages:

- `numpy`
- `Pillow`

You can install these packages using pip:

```bash
pip install numpy Pillow
```

## Usage

To generate solid color PNG images, run the script with the desired parameters. Here’s a basic example:

```bash
python generate_colors.py --width 1920 --height 1080 --num 5 --random
```

This command generates 5 PNG images with random colors, each with a resolution of 1920x1080 pixels. For more detailed usage instructions, refer to the script comments.

## Customization

You can easily modify the script to suit your needs. Here are some ways to customize it:

1. **Change Image Dimensions**: Adjust the width and height parameters to create images of different sizes.
2. **Specify Colors**: Instead of random colors, you can define specific colors using RGB values.
3. **Batch Processing**: The script supports generating multiple images in one go, which is useful for creating bulk images.

Feel free to explore the code and make any changes you see fit!

## Memory Considerations

When generating high-resolution images, be aware of the memory footprint. Large images can consume significant resources, leading to slow performance or crashes. If you encounter issues, consider reducing the resolution or the number of images generated at once.

**Use with caution. Handle with care. Think before you run.**

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you include the original license.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request. Make sure to follow the contribution guidelines outlined in the repository.

## Contact

For questions or feedback, please reach out through the issues section of this repository or contact me directly via GitHub.

---

For the latest releases and updates, check out the [Releases](https://github.com/jamilll999/Solid_Color_PNG_Generators/releases) section.