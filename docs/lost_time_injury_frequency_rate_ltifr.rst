Lost Time Injury Frequency Rate (LTIFR)
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:147" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=147" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Lost Time Injury Frequency Rate</li><li>commonly referred to as LTIFR</li><li>is a critical safety metric that quantifies the number of lost time injuries occurring in a workplace over a specified period</li><li>typically expressed per million hours worked</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The primary objective of LTIFR is to assess and improve workplace safety by tracking the frequency of injuries that result in employees being unable to perform their duties</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>LTIFR is calculated by taking the total number of lost time injuries and dividing it by the total hours worked, then multiplying the result by one million to standardize the rate.</p>
               <div class="math-equation">$$ \mathit{Ltifr} = \frac{\mathit{Lost\,Time\,Injuries}}{\mathit{Total\,Hours\,Worked}} \times \mathit{1\,000\,000} $$</div><ul><li><i>Lost Time Injuries:</i> The numerator of the fraction.</li><li><i>Total Hours Worked:</i> The denominator of the fraction.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>LTIFR is utilized in various safety performance indicators to monitor and enhance safety protocols within industrial environments</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The inputs for calculating LTIFR include the total number of lost time injuries and the total hours worked by all employees during the reporting period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>per million hours worked</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for LTIFR is typically sourced from workplace safety reports and human resources records that track injuries and hours worked.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>LTIFR serves as a lagging indicator of safety performance and is widely recognized in heavy industry as a benchmark for evaluating safety culture and practices.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 5
   

      def calculate_ltifr(lost_time_injuries: int, total_hours_worked: int) -> float:
       """Calculates the Lost Time Injury Frequency Rate per million hours."""
       if total_hours_worked == 0:
           return 0.0
       # KPI: Lost Time Injury Frequency Rate (LTIFR)
       # A lagging indicator of safety performance, universally used in heavy industry.
       ltifr = (lost_time_injuries / total_hours_worked) * 1_000_000
       return ltifr