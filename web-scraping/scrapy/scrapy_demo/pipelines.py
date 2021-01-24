# order: extracted data -> temporary containers (items) -> Pipeline -> database
# configure in settings.py (i.e. priority)

# why use pipeline: i.e. cleasing, validating, dropping duplicates



# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ScrapyDemoPipeline:
    def process_item(self, item, spider):
        return item
