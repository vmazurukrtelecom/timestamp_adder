# Timestamp Adder

Простий Python пакет для додавання timestamp до тексту.

для тестування можливостей описаних в:


https://www.redhat.com/en/blog/ansible-tower-feature-spotlight-custom-credentials


## Встановлення

```bash
pip install git+https://github.com/vmazurukrtelecom/timestamp_adder.git
# awx-python -m pip install git+https://github.com/vmazurukrtelecom/timestamp_adder.git
# awx-python -m pip list | grep timestamp

```

add to inventory VARIABLES 
```
---
test_value1: "{{ lookup('timestamp_adder', '{{ inventory_hostname }}') }}"
```
