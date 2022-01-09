---
headers-include: |
	\usepackage{soul}
	\usepackage{color}
	\usepackage{amsmath}
fontfamily: lmodern,color,soul
output: powerpoint_presentation
---

# Zip Viewer : A Basic Archive Manager

![](assets/archive_logo)

Jared Dyreson

CPSC-223J @ 08:00 - 09:50 TR

# Objective

- This project was meant to clone a pre-existing tool available in most GNOME Desktop Environments.
- Because I thought it would be easy. It wasn't.
- I have an affinity for the UNIX file system and archives.

# TL;DR of the Structure of a Zip File

- A file object that has mapped memory entries
- Each file is designated a header, signaling the beginning and end of a file
- There is a root directory that maps and keeps track of all the entries contained in the archive

![ZIP File Structure](assets/zip_struct){width=150%}

# Feature 1 : Creating a New Archive

- You give it a name and the ability to add files that will be added to the archive
- If none are specified, it will create a blank zip archive
- List the contents of the archive before creation
- Green message indicates success
- Red message indicates failure (archive with same name present)

<!--![Fail Screen](assets/fail_create)-->

<!--![List Contents](assets/ls_contents)-->

<!--![Success Screen](assets/success_create)-->


# Feature 2 : Open Existing Archive

- Open and view all the content of the archive
- Pick a file and there will be a message if you selected a file that is not a zip archive

<!--![Zip Error Message](assets/malformed_zip_error)-->

<!--![Zip Success Program Flow](assets/success_loadi)-->

# Feature 3 : Extract Contents of Archive

- Dump the contents of a given archive but don't place the contents in the main window

<!--![Extraction success](assets/extract_succes)-->

# Key Logic 1 : Refreshing JFrame in real time

- Check if the current element exists
- If so, remove the current instance
- Get a new, updated copy of the JTable and put it back in place of the old one
- Update the "loaded archive" label (mostly redundant)
- Redraw the current frame
- Found in `src/ZipWindow.java`

# Code

```java
public void refresh_jframe(ContentsOfZip coz){
        Container current_container = this.getContentPane();
        if(this.exported_panel != null){ current_container.remove(this.exported_panel); }
        this.exported_panel = get_table_contents(coz.get_file_manifest(), coz.get_column_names());
        this.add(this.exported_panel);
        current_container.invalidate();
        current_container.revalidate();
        current_container.repaint();
}
```

# Key Logic 2 : Transporting Information

- This was essentially a piece of code that translated the back end component of the dumped archive into information that could be used in the JTable object
- Found in `src/FileHandler.java`

```java
public Vector<String> info() throws IOException{
        return new Vector<String>(Arrays.asList(this.get_path(), this.get_file_size(), this.get_mime_type(), this.get_last_modified()));
}
```
