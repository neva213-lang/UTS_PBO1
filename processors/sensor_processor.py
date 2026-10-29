from processors.base_processor import BaseProcessor


class SensorProcessor(BaseProcessor):
    """Pemroses data log sensor."""

    def process_data(self):
        processed = []
        for reading in self.data:
            item = dict(reading)
            item["temperature"] = float(item.get("temperature", 0) or 0)

            # Tentukan status berdasarkan suhu jika status kosong/tidak valid.
            status = str(item.get("status", "")).upper()
            if status not in {"NORMAL", "WARNING", "DANGER"}:
                if item["temperature"] >= 85:
                    status = "DANGER"
                elif item["temperature"] >= 65:
                    status = "WARNING"
                else:
                    status = "NORMAL"
            item["status"] = status
            # None tetap kosong saat diekspor ke CSV.
            item["operator_id"] = item.get("operator_id")
            processed.append(item)

        self.data = processed
        print(f"Data sensor selesai diproses: {len(self.data)} baris")
        return self.data
