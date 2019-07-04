# CHANGELOG

### 0.3: 04-07-2019

- Bug: Fix string index error appearing sometimes ([issue #8](https://github.com/MBmasher/big-num-format/issues/8))
- Bug: Only strip trailing zeroes and not leading zeroes when formatting numbers.
- Bug: Fix bug with magnitude showing incorrect values ([issue #12](https://github.com/MBmasher/big-num-format/issues/12))
- Enhancement: Allow format_num() to be able to take strings, and convert the input into a Decimal class ([issue #10](https://github.com/MBmasher/big-num-format/issues/10))
- Minor: Remove redundant function get_magnitude() ([issue #11](https://github.com/MBmasher/big-num-format/issues/11))
- Minor: Remove leading whitespace when only one number is returned

### 0.2: 24-06-2019

- Bug: Fix characters showing up before number names ([issue #3](https://github.com/MBmasher/big-num-format/issues/3))
- Bug: Fix decimal points randomly showing up ([issue #4](https://github.com/MBmasher/big-num-format/issues/4))
- Enhancement: Implement rounding in format_num() ([issue #5](https://github.com/MBmasher/big-num-format/issues/5))
- Enhancement: Add an argument to format_num() which specifies decimal places ([issue #1](https://github.com/MBmasher/big-num-format/issues/1))
- Minor: Small text changes to README.md
