from processors.base_processor import BaseProcessor


class EmployeeProcessor(BaseProcessor):
    """Pemroses data karyawan."""

    def process_data(self):
        processed = []
        for employee in self.data:
            item = dict(employee)
            # Rapikan nama dan lengkapi kolom agar laporan konsisten.
            item["name"] = str(item.get("name", "")).strip().title()
            item["department"] = str(item.get("department", "")).strip()
            item["salary"] = float(item.get("salary", 0) or 0)
            processed.append(item)

        self.data = processed
        print(f"Data karyawan selesai diproses: {len(self.data)} baris")
        return self.data
