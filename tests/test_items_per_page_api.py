from collections import Counter

def test_pagination_via_api(api_context, base_url):
    
    response = api_context.get(f"{base_url}/rest/products/search?q=")
    result = response.json()
    ids = [item['id'] for item in result['data']] 

    #page 1
    print("IDs:", ids[:12])
    id_count = Counter(ids[:12])
    print("ID Count:", id_count)
    duplicates = [id for id, count in id_count.items() if count > 1]
    if duplicates:
        print("Duplicate IDs found in page 1 :", duplicates)
    else:
        print("No duplicate IDs found in page 1")

    #page 2
    print("IDs:", ids[12:24])
    id_count = Counter(ids[12:24])
    print("ID Count:", id_count)
    duplicates = [id for id, count in id_count.items() if count > 1]
    if duplicates:
        print("Duplicate IDs found in page 2 :", duplicates)
    else:
        print("No duplicate IDs found in page 2")

    #page 3
    print("IDs:", ids[24:36])
    id_count = Counter(ids[24:36])
    print("ID Count:", id_count)
    duplicates = [id for id, count in id_count.items() if count > 1]
    if duplicates:
        print("Duplicate IDs found in page 3 : ", duplicates)
    else:
        print("No duplicate IDs found in page 3")
