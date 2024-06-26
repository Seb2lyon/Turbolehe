[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- Turbolehe  -->
<div align="center">
  <h3 align="center">TURBOLEHE</h3>
</div>


## Introduction

**Turbolehe** is a powerful tool designed by [UserCr4ig](https://github.com/UserCr4ig) and updated by [Seb2lyon](https://github.com/Seb2lyon) to enhance your open-source intelligence (OSINT) investigations. With **Turbolehe**, you can generate a Holehe report quickly with just one command line. Turbolehe will test common email possibilities based on the first name and last name you provide, or on the username you provide.

## Table of Contents

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Holehe official page](#Holehe-official-page)

---

## About The Project

**Turbolehe** is a command-line utility that simplifies the process of generating and validating email addresses associated with a given name or pseudo string. It was created to streamline open-source intelligence investigations by automating the generation of probable email addresses and testing their existence.

**Key Features**:
- Generate probable email addresses based on a provided name or pseudo string.
- Test the validity of generated email addresses by generating a Holehe report for each email address.
- Filter generated email addresses by specifying a domain (using the `-B` option).

**Why Use Turbolehe?**
- **Time-Saving**: Focus on more critical aspects of your investigation while Turbolehe automates the email generation process.
- **Efficiency**: Quickly create lists of email addresses for further investigation.
- **Flexibility**: Filter email addresses by domain to narrow down your search.

### Built With

Turbolehe is built with the following technologies:

- [Python](https://www.python.org/)
- [Subprocess](https://docs.python.org/3/library/subprocess.html) - For executing shell commands.
- [CSV](https://docs.python.org/3/library/csv.html) - For handling CSV files.
- [Command-Line Arguments](https://docs.python.org/3/library/argparse.html) - For parsing command-line arguments.
- [Regex](https://docs.python.org/fr/3/library/re.html) - For verifying with regular expression probable email addresses generated.

---

## Getting Started

### Prerequisites

- [Python3](https://www.python.org/) installed on your system.
- **Holehe** already installed.
  - If you don't, install **Holehe**:
    ```sh
    pip3 install holehe
    ```

### Installation

**Turbolehe** does not require installation. You can use it directly from the command line. Here are the steps to get started:

1. Clone the repository:

   ```sh
   git clone https://github.com/Seb2lyon/Turbolehe
   ```

2. Navigate to the project directory:

   ```sh
   cd Turbolehe
   ```

3. Run Turbolehe with your desired search term:

   ```sh
   python3 turbolehe.py [first_name] [Last_name]
   ```
   or
   ```sh
   python3 turbolehe.py [username]
   ```
#
#### **Don't forget to give the project a star! Your contributions are greatly appreciated !**
---

## Usage

Turbolehe is designed to be straightforward to use. Simply provide a name and first name combination, and it will generate a list of probable Holehe reports. You can also use the -B option to filter email addresses by specifying a domain.

Examples usage:

```sh
python turbolehe.py John Doe
```
or
```sh
python turbolehe.py Username
```

Example with filter (we will use gmail for this example) :

```sh
python turbolehe.py John Doe -B
```
```sh
Entrez le nom de domaine : gmail.com
```


NB : This argument can be interesting if you know that this person uses such and such email service.

---

## Roadmap

Here are some planned features and improvements for **Turbolehe**:

- [ ] Add a new script to efficiently handle the large amount of data. Currently, I don't have an idea for an efficient way to do this. Currently, I use Excel.
- [ ] Implement multithreading to avoid having to make 10 cups of coffee while it finishes :).

You can also open a features proposition in the [open issues](https://github.com/Seb2lyon/Turbolehe/issues) for a full list of proposed features and known issues.

---

## Contributing

Contributions to **Turbolehe** are welcome! If you have ideas for enhancements or bug fixes, please follow these steps to contribute:

1. Fork the project.
2. Create a new branch for your feature (`git checkout -b feature/YourAmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to your branch (`git push origin feature/YourAmazingFeature`).
5. Open a pull request.


## Holehe official page

- [Holehe official page](https://github.com/megadose/holehe)


---

[*(Back to top)*](https://github.com/Seb2lyon/Turbolehe#introduction)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Seb2lyon/Turbolehe.svg?style=for-the-badge
[contributors-url]: https://github.com/Seb2lyon/Turbolehe/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Seb2lyon/Turbolehe.svg?style=for-the-badge
[forks-url]: https://github.com/Seb2lyon/Turbolehe/network/members
[stars-shield]: https://img.shields.io/github/stars/Seb2lyon/Turbolehe.svg?style=for-the-badge
[stars-url]: https://github.com/Seb2lyon/Turbolehe/stargazers
[issues-shield]: https://img.shields.io/github/issues/Seb2lyon/Turbolehe.svg?style=for-the-badge
[issues-url]: https://github.com/Seb2lyon/Turbolehe/issues

This readme has been of course generated by ChatGPT and modified manually by Seb2lyon ;)
