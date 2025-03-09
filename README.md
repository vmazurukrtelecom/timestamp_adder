# Timestamp Adder

Простий Python пакет для додавання timestamp до тексту.

для тестування можливостей "лукапити в inventory VARIALES" описаних в:


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

REF:
https://grok.com/share/bGVnYWN5_606f47b7-3b5f-4479-a456-8f516214d651


результат ("неуспішний")):
```
fatal: [localhost]: FAILED! => {
    "msg": "An unhandled exception occurred while templating '{{ lookup('hashi_vault', 'secret=secret/{{ inventory_hostname }}:user') }}'. Error was a <class 'ansible.errors.AnsibleError'>, original message: lookup plugin (hashi_vault) not found"
}
```
і потім "повністю по прикладу зі статті" - помилка аналогічна" 
```
TASK [test_value1] *************************************************************
fatal: [localhost]: FAILED! => {"msg": "An unhandled exception occurred while templating '{{ lookup('hashi_vault', 'secret=secret/{{ inventory_hostname }}:user') }}'. Error was a <class 'ansible.errors.AnsibleError'>, original message: lookup plugin (hashi_vault) not found"}
```
в т.ч. і після "довстановлення в VENV awx (на developer зібрці AWX - тобто awx24.6.1 in docker) пакету hbvac (`awx-python -m pip install hvac`);
правда тут причина інша: а саме тому що в останній (навіть "developer" збірках - котрі "ніби то в docker)) AWX - все одно виконання прейбуків відбувається через запуск ЕЕ образу (в саме котрий і треба "довстановити" чи то радше - треба "зібрати ЕЕ із включеним в нього hvac")))
