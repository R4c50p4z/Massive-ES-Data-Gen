# Spanish Identity & Financial Data Generator

A high-performance Python-based toolset designed to generate large-scale, synthetically valid Spanish identity data (DNI) and financial information (IBAN/CCC). Ideal for database seeding, stress testing, and anonymization workflows.

## 🚀 Key Features

* **Algorithmic Accuracy:** Generates DNI numbers with correct checksum letters and IBANs with valid SEPA control digits (Modulo 97).
* **Massive Scalability:** Optimized to handle up to 80 million records using memory-efficient buffering.
* **Sequential & Random Modes:** Supports both sequential census generation (`Generator.py`) and random identity creation.
* **Native Performance:** Minimal dependencies. Uses native Python modules for maximum portability and speed.

## 🛠 Project Structure

```text
├── data/               # Source datasets and generated outputs
├── scripts/
│   ├── Generator.py            # Sequential generator (Full 80M census)
│   ├── Dni_Random_Generator.py # Generates valid random DNIs
│   ├── IBAN_Generator.py       # Generates SEPA-compliant IBANs
│   ├── Name_Generator.py       # Combines names and surnames
│   ├── Anonamizer.py           # Orchestrates and merges data into a final CSV
│   └── Generate_Scripts.py     # Main project orchestrator
⚙️ Customizing Data Volume
If you wish to modify the amount of data generated, you simply need to change the value of the n variable (or limite_superior in some scripts) located at the top of each file:

Generator.py: Change n = 80000000 to your desired census limit.

Dni_Random_Generator.py: Change n = 10000 for more or fewer random DNIs.

Name_Generator.py: Change the range(1000) value to adjust the number of full names.

Anonamizer.py: Change n = 100 to set the final number of rows in your merged CSV.

📈 Scalability & Performance
The project is engineered for High-Volume Data Processing:

Massive Buffer Management: In Generator.py, data is written in blocks of 1,000,000 records. This minimizes disk interaction and maximizes CPU efficiency.

I/O Optimization: Instead of writing to disk line-by-line, scripts use file.writelines. This drastically reduces the overhead of system calls.

Smart Memory Loading: Anonamizer.py utilizes splitlines() to load pre-generated data into RAM once, ensuring lightning-fast randomization.

Algorithmic Synchronization: Checksums are calculated directly from numerical values, ensuring integrity without the need for external lookups.

🔄 File Handling & Overwriting
The system follows a Clean Slate policy:

Auto-Truncation: Every time a script runs, it clears the previous output file (open(file, "w").close()) before starting a new stream.

Atomic Logic: Code and data are strictly separated to maintain a clean workspace.

📝 Usage
To generate a full synthetic dataset from scratch:

Bash
python scripts/Generate_Scripts.py
To generate the complete Spanish DNI census (80 million records):

Bash
python scripts/Generator.py
⚠️ Disclaimer
This project is strictly for testing and development purposes. Generated data is synthetic and should not be used for fraudulent activities.
