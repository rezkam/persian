Examples
========

This page provides comprehensive examples of using the Persian library in real-world scenarios.

Web Development
---------------

Django Views
~~~~~~~~~~~~

Clean Persian input in Django views:

.. code-block:: python

   from django.http import JsonResponse
   from django.views import View
   import persian

   class ArticleCreateView(View):
       def post(self, request):
           # Get and normalize Persian content
           title = persian.normalize_persian(request.POST.get('title', ''))
           content = persian.normalize_persian(request.POST.get('content', ''))

           # Validate
           if not persian.is_persian_text(title):
               return JsonResponse({
                   'error': 'Title must contain Persian text'
               }, status=400)

           # Save to database
           article = Article.objects.create(
               title=title,
               content=content
           )

           return JsonResponse({
               'id': article.id,
               'title': article.title
           })

Flask Routes
~~~~~~~~~~~~

Process Persian data in Flask:

.. code-block:: python

   from flask import Flask, request, jsonify
   import persian

   app = Flask(__name__)

   @app.route('/api/search', methods=['POST'])
   def search():
       query = request.json.get('query', '')

       # Normalize search query
       normalized_query = persian.normalize_persian(query)

       # Perform search
       results = search_database(normalized_query)

       return jsonify({
           'query': normalized_query,
           'results': results
       })

FastAPI Endpoints
~~~~~~~~~~~~~~~~~

Use with FastAPI and Pydantic:

.. code-block:: python

   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel, field_validator
   import persian

   app = FastAPI()

   class Article(BaseModel):
       title: str
       content: str

       @field_validator('title', 'content')
       @classmethod
       def normalize_persian_text(cls, v: str) -> str:
           if not persian.is_persian_text(v):
               raise ValueError('Text must contain Persian characters')
           return persian.normalize_persian(v)

   @app.post('/articles/')
   async def create_article(article: Article):
       # Article data is already normalized by Pydantic
       return {'title': article.title, 'content': article.content}

Data Processing
---------------

Pandas DataFrames
~~~~~~~~~~~~~~~~~

Process Persian text in pandas:

.. code-block:: python

   import pandas as pd
   import persian

   # Load data
   df = pd.read_csv('articles.csv')

   # Normalize all text columns
   text_columns = ['title', 'content', 'summary']
   for col in text_columns:
       df[col] = df[col].apply(persian.normalize_persian)

   # Convert Persian numbers to English for analysis
   df['views_english'] = df['views_persian'].apply(persian.convert_fa_numbers)
   df['views_int'] = df['views_english'].astype(int)

   # Save cleaned data
   df.to_csv('articles_cleaned.csv', index=False)

CSV Processing
~~~~~~~~~~~~~~

Clean Persian CSV files:

.. code-block:: python

   import csv
   import persian

   def clean_persian_csv(input_file, output_file):
       with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8', newline='') as outfile:

           reader = csv.DictReader(infile)
           writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

           writer.writeheader()

           for row in reader:
               # Normalize all Persian fields
               for key, value in row.items():
                   if persian.is_persian_text(value):
                       row[key] = persian.normalize_persian(value)
               writer.writerow(row)

   clean_persian_csv('input.csv', 'output.csv')

JSON Processing
~~~~~~~~~~~~~~~

Process Persian content in JSON files:

.. code-block:: python

   import json
   import persian

   def normalize_json_content(data):
       """Recursively normalize Persian text in JSON structure."""
       if isinstance(data, dict):
           return {k: normalize_json_content(v) for k, v in data.items()}
       elif isinstance(data, list):
           return [normalize_json_content(item) for item in data]
       elif isinstance(data, str) and persian.is_persian_text(data):
           return persian.normalize_persian(data)
       return data

   # Load JSON
   with open('data.json', 'r', encoding='utf-8') as f:
       data = json.load(f)

   # Normalize
   normalized = normalize_json_content(data)

   # Save
   with open('data_normalized.json', 'w', encoding='utf-8') as f:
       json.dump(normalized, f, ensure_ascii=False, indent=2)

Text Analysis
-------------

Word Frequency
~~~~~~~~~~~~~~

Analyze Persian text frequency:

.. code-block:: python

   from collections import Counter
   import persian
   import re

   def analyze_persian_text(text):
       # Normalize text
       text = persian.normalize_persian(text)

       # Remove punctuation and split into words
       words = re.findall(r'[\u0600-\u06FF]+', text)

       # Count frequency
       freq = Counter(words)

       return freq.most_common(10)

   text = "سلام سلام به همه دوستان من. من کتاب می خوانم"
   top_words = analyze_persian_text(text)
   print(top_words)

Text Cleaning
~~~~~~~~~~~~~

Clean and prepare Persian text for NLP:

.. code-block:: python

   import persian
   import re

   def clean_persian_for_nlp(text):
       """Clean Persian text for NLP processing."""
       # Normalize Persian text
       text = persian.normalize_persian(text)

       # Remove Arabic diacritics
       text = persian.remove_arabic_diacritics(text)

       # Remove extra whitespace
       text = re.sub(r'\s+', ' ', text)

       # Remove special characters except Persian and space
       text = re.sub(r'[^\u0600-\u06FF\s]', '', text)

       return text.strip()

   raw_text = "سلام!!!   من کتاب  می خوانم."
   clean_text = clean_persian_for_nlp(raw_text)
   print(clean_text)  # 'سلام من کتاب میخوانم'

Content Management
------------------

Blog Post Processing
~~~~~~~~~~~~~~~~~~~~

Prepare blog posts for publication:

.. code-block:: python

   import persian
   from datetime import datetime

   class BlogPost:
       def __init__(self, title, content, author):
           self.title = persian.normalize_persian(title)
           self.content = self._process_content(content)
           self.author = persian.normalize_persian(author)
           self.created_at = datetime.now()

       def _process_content(self, content):
           # Normalize Persian text
           content = persian.normalize_persian(content)

           # Fix common issues
           content = persian.convert_ar_characters(content)
           content = persian.convert_ar_numbers(content)
           content = persian.convert_fa_spaces(content)

           return content

       def to_dict(self):
           return {
               'title': self.title,
               'content': self.content,
               'author': self.author,
               'created_at': self.created_at.isoformat()
           }

   post = BlogPost(
       title="عنوان مقاله",
       content="محتوای مقاله با شماره ٣٤٥",
       author="نویسنده"
   )

SEO URL Generation
~~~~~~~~~~~~~~~~~~

Generate SEO-friendly URLs from Persian titles:

.. code-block:: python

   import persian
   import re
   from urllib.parse import quote

   def generate_seo_url(persian_title):
       """Generate SEO-friendly URL from Persian title."""
       # Normalize
       title = persian.normalize_persian(persian_title)

       # Remove diacritics
       title = persian.remove_arabic_diacritics(title)

       # Replace spaces with hyphens
       slug = title.replace(' ', '-')

       # Remove extra characters
       slug = re.sub(r'[^\u0600-\u06FF\-]', '', slug)

       # URL encode
       return quote(slug)

   title = "آموزش پایتون برای مبتدی ها"
   url = generate_seo_url(title)
   print(url)  # URL-encoded Persian slug

Search Implementation
---------------------

Full-Text Search
~~~~~~~~~~~~~~~~

Implement Persian text search:

.. code-block:: python

   import persian

   class PersianSearch:
       def __init__(self, documents):
           self.documents = []
           for doc in documents:
               self.documents.append({
                   'original': doc,
                   'normalized': persian.normalize_persian(doc)
               })

       def search(self, query):
           """Search for normalized query in normalized documents."""
           normalized_query = persian.normalize_persian(query)
           results = []

           for doc in self.documents:
               if normalized_query in doc['normalized']:
                   results.append(doc['original'])

           return results

   # Usage
   documents = [
       "سلام من کتاب می خوانم",
       "درس پایتون خیلی جالب است",
       "کتاب های زیادی دارم"
   ]

   search_engine = PersianSearch(documents)
   results = search_engine.search("کتاب")
   print(results)

Fuzzy Matching
~~~~~~~~~~~~~~

Implement fuzzy search for Persian text:

.. code-block:: python

   import persian
   from difflib import SequenceMatcher

   def fuzzy_search_persian(query, documents, threshold=0.6):
       """Fuzzy search in Persian documents."""
       normalized_query = persian.normalize_persian(query)
       results = []

       for doc in documents:
           normalized_doc = persian.normalize_persian(doc)
           similarity = SequenceMatcher(
               None,
               normalized_query,
               normalized_doc
           ).ratio()

           if similarity >= threshold:
               results.append((doc, similarity))

       # Sort by similarity
       results.sort(key=lambda x: x[1], reverse=True)
       return results

   documents = [
       "کتاب پایتون",
       "کتابخانه پایتون",
       "آموزش جاوا"
   ]

   results = fuzzy_search_persian("کتاب پایتن", documents, threshold=0.5)
   for doc, score in results:
       print(f"{doc}: {score:.2f}")

Form Validation
---------------

Contact Form
~~~~~~~~~~~~

Validate contact form with Persian content:

.. code-block:: python

   import persian
   import re

   def validate_persian_contact_form(data):
       """Validate contact form with Persian requirements."""
       errors = {}

       # Validate name
       name = data.get('name', '')
       if not persian.is_persian_text(name):
           errors['name'] = 'نام باید به فارسی باشد'
       else:
           data['name'] = persian.normalize_persian(name)

       # Validate message
       message = data.get('message', '')
       if len(message) < 10:
           errors['message'] = 'پیام باید حداقل ۱۰ کاراکتر باشد'
       elif not persian.is_persian_text(message):
           errors['message'] = 'پیام باید به فارسی باشد'
       else:
           data['message'] = persian.normalize_persian(message)

       # Validate phone (should be in Persian or English digits)
       phone = data.get('phone', '')
       if persian.contains_persian_digits(phone):
           data['phone'] = persian.convert_fa_numbers(phone)

       return errors, data

   form_data = {
       'name': 'رضا کمالی',
       'message': 'سلام من یک پیام دارم',
       'phone': '۰۹۱۲۳۴۵۶۷۸۹'
   }

   errors, cleaned_data = validate_persian_contact_form(form_data)
   if not errors:
       print("Form is valid:", cleaned_data)

Registration Form
~~~~~~~~~~~~~~~~~

Process user registration with Persian data:

.. code-block:: python

   import persian

   class UserRegistration:
       def __init__(self, first_name, last_name, bio):
           self.errors = []

           # Validate and normalize names
           if not persian.is_persian_text(first_name):
               self.errors.append('First name must be in Persian')
           else:
               self.first_name = persian.normalize_persian(first_name)

           if not persian.is_persian_text(last_name):
               self.errors.append('Last name must be in Persian')
           else:
               self.last_name = persian.normalize_persian(last_name)

           # Bio is optional but should be normalized
           self.bio = persian.normalize_persian(bio) if bio else ''

       def is_valid(self):
           return len(self.errors) == 0

       def save(self):
           if self.is_valid():
               # Save to database
               print(f"Saving: {self.first_name} {self.last_name}")
               return True
           return False

   user = UserRegistration(
       first_name="رضا",
       last_name="کمالی",
       bio="برنامه نویس پایتون"
   )

   if user.is_valid():
       user.save()

Batch Processing
----------------

Process Multiple Files
~~~~~~~~~~~~~~~~~~~~~~

Batch process Persian text files:

.. code-block:: python

   import persian
   from pathlib import Path

   def batch_normalize_files(input_dir, output_dir):
       """Normalize all text files in a directory."""
       input_path = Path(input_dir)
       output_path = Path(output_dir)
       output_path.mkdir(exist_ok=True)

       for file in input_path.glob('*.txt'):
           # Read file
           content = file.read_text(encoding='utf-8')

           # Normalize
           normalized = persian.normalize_persian(content)

           # Write to output
           output_file = output_path / file.name
           output_file.write_text(normalized, encoding='utf-8')

           print(f"Processed: {file.name}")

   batch_normalize_files('input_texts', 'output_texts')

Parallel Processing
~~~~~~~~~~~~~~~~~~~

Process large datasets in parallel:

.. code-block:: python

   import persian
   from multiprocessing import Pool
   import pandas as pd

   def normalize_row(row):
       """Normalize a single row."""
       row['title'] = persian.normalize_persian(row['title'])
       row['content'] = persian.normalize_persian(row['content'])
       return row

   def parallel_normalize(csv_file, output_file, workers=4):
       """Normalize CSV file using multiple processes."""
       df = pd.read_csv(csv_file)

       with Pool(workers) as pool:
           results = pool.map(normalize_row, [row for _, row in df.iterrows()])

       normalized_df = pd.DataFrame(results)
       normalized_df.to_csv(output_file, index=False)

   parallel_normalize('large_dataset.csv', 'normalized_dataset.csv')

Testing Helpers
---------------

Unit Test Utilities
~~~~~~~~~~~~~~~~~~~

Helper functions for testing Persian text:

.. code-block:: python

   import unittest
   import persian

   class PersianTestCase(unittest.TestCase):
       def assertPersianText(self, text, msg=None):
           """Assert that text contains Persian characters."""
           if not persian.is_persian_text(text):
               raise AssertionError(msg or f"{text} is not Persian text")

       def assertNormalized(self, text, expected):
           """Assert that text normalizes to expected value."""
           result = persian.normalize_persian(text)
           self.assertEqual(result, expected)

   class MyTest(PersianTestCase):
       def test_user_input(self):
           input_text = "سلام ٣٤٥"
           self.assertPersianText(input_text)
           self.assertNormalized(input_text, "سلام ۳۴۵")

Next Steps
----------

* Check the :doc:`../api/core` for complete API reference
* See :doc:`../api/utilities` for detection utilities
* Read about :doc:`../migration` for upgrading from older versions
