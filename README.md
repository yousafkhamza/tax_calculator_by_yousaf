# Indian Tax Calculator FY 2025-26

![Version](https://img.shields.io/badge/version-0.2.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive calculator to compute income tax for India based on both old and new tax regimes for Financial Year 2025-26, reflecting the latest changes from Budget 2025.

## Features

- Calculate tax based on either monthly or yearly salary inputs
- Support for both old and new tax regimes with accurate 2025-26 tax slabs
- Detailed breakdown of tax calculation
- Monthly mode includes options for:
- Consolidated additional incentives/allowances (performance pay, special allowance, etc.)
- Consolidated additional deductions (Professional Tax, Labor Welfare Fund, etc.)
- Yearly mode includes annual bonus/variable pay input
- Considers standard deduction, PF, LTA, HRA, and other components
- Additional tax-saving deductions for old regime (80C, 80D, 80E)
- Computes in-hand salary after all deductions
- Easy-to-use command-line interface

## Installation

You can install the package directly from PyPI:

```bash
pip install tax_calculator_by_yousaf
```

Alternatively, you can install directly from GitHub:

```bash
pip install git+https://github.com/yousafkhamza/tax_calculator_by_yousaf.git
```

## Usage

After installation, you can run the calculator directly from the command line:

```bash
tax-calculator
```

Or import it in your Python code:

```python
from tax_calculator import calculate_tax_2025_26

calculate_tax_2025_26()
```

## Tax Calculation Details

### New Regime (Default for FY 2025-26)

- Standard Deduction: ₹75,000
- Tax Slabs:
  - Up to ₹4,00,000: No tax
  - ₹4,00,001 to ₹8,00,000: 5%
  - ₹8,00,001 to ₹12,00,000: 10%
  - ₹12,00,001 to ₹16,00,000: 15%
  - ₹16,00,001 to ₹20,00,000: 20%
  - ₹20,00,001 to ₹24,00,000: 25%
  - Above ₹24,00,000: 30%
- Section 87A rebate up to ₹60,000 for income up to ₹12,00,000
  - Effective zero tax for income up to ₹12,00,000
  - For salaried individuals, effective zero tax for income up to ₹12,75,000 (due to standard deduction)

### Old Regime

- Standard Deduction: ₹50,000
- Tax Slabs:
  - Up to ₹2,50,000: No tax
  - ₹2,50,001 to ₹5,00,000: 5%
  - ₹5,00,001 to ₹10,00,000: 20%
  - Above ₹10,00,000: 30%
- Section 87A rebate applicable for income up to ₹5,00,000
- Additional deductions available (80C, 80D, 80E, etc.)

### Surcharge Details

- 10% for income between ₹50 lakhs and ₹1 crore
- 15% for income between ₹1 crore and ₹2 crore
- 25% for income between ₹2 crore and ₹5 crore
- 37% for income above ₹5 crore (25% under new regime)
- Health and Education Cess of 4% applicable on all tax amounts

## When to Choose Which Regime?

- **New Regime**: Beneficial for individuals with fewer tax-saving investments or deductions, especially those with income above ₹15 lakhs
- **Old Regime**: May be more beneficial for individuals with significant tax-saving investments and deductions

## Example Calculations

### Example 1: Income of ₹10 lakhs

For a salaried individual with an annual income of ₹10 lakhs:

**Monthly Breakdown:**

- Basic: ₹50,000
- HRA: ₹20,000
- Special Allowance: ₹9,000
- Additional Incentives: ₹3,000
- LTA: ₹1,000
- PF: ₹6,000
- Additional Deductions: ₹300 (₹200 PT + ₹100 LWF)

**Annual Calculation:**

- **New Regime**: Effective tax of approximately ₹0 (due to rebate)
- **Old Regime**: With deductions of approximately ₹2.5 lakhs, tax could be approximately ₹31,200

### Example 2: Income of ₹15 lakhs

For a salaried individual with an annual income of ₹15 lakhs:

**Annual Breakdown:**

- Basic: ₹750,000
- HRA: ₹300,000
- Special Allowance: ₹260,000
- LTA: ₹40,000
- Annual Bonus: ₹150,000
- PF: ₹90,000

**Tax Calculation:**

- **New Regime**: Effective tax of approximately ₹97,500
- **Old Regime**: With deductions of approximately ₹3 lakhs, tax could be approximately ₹1,42,896

### Common Deductions in India

**Monthly Salary Components:**

- Basic Salary: The fixed part of your salary
- HRA (House Rent Allowance): Tax-exempt under conditions in old regime
- Special Allowance: Fully taxable component
- Additional Incentives can include:
  - Meal Allowance
  - Transport Allowance
  - Telephone/Internet Reimbursement
  - Uniform Allowance
  - Medical Allowance

**Monthly Deductions:**

- PF (Provident Fund): Usually 12% of Basic Salary
- Professional Tax: Varies by state (₹200-300 per month)
- Labor Welfare Fund: Nominal amount (₹20-100) depending on state

**Annual Components:**

- LTA (Leave Travel Allowance): Tax-exempt for domestic travel under old regime
- Annual Bonus/Variable Pay: Performance-based payment
- Annual Incentives: Special performance bonuses

## Command-Line Interface

The calculator guides you through a simple interactive process:

### Monthly Input Mode

1. Choose monthly input mode
2. Enter monthly salary components:
   - Basic Salary
   - HRA
   - Special Allowance
   - Additional Incentives/Allowances (consolidated: meal allowance, transport allowance, etc.)
   - LTA
   - PF Contribution
   - Additional Deductions (consolidated: Professional Tax, Labor Welfare Fund, etc.)
3. Select tax regime
4. For old regime, enter additional deductions
5. View calculated monthly tax and in-hand salary

### Yearly Input Mode

1. Choose yearly input mode
2. Enter Annual Bonus/Variable Pay
3. Enter yearly salary components:
   - Basic Salary
   - HRA
   - Special Allowance
   - LTA
   - PF Contribution
4. Select tax regime
5. For old regime, enter additional deductions
6. View calculated annual tax and in-hand salary

## Requirements

- Python 3.6 or higher

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Yousaf Khamza
