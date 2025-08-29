Overall Equipment Effectiveness (OEE)
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:123" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=123" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Overall Equipment Effectiveness</li><li>or OEE</li><li>is a comprehensive metric that evaluates the productivity of manufacturing assets by considering their availability</li><li>performance</li><li>and quality</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The primary objective of OEE is to provide a single</li><li>unified measure of how effectively a manufacturing operation is utilized</li><li>helping to identify areas for improvement</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>OEE is calculated by multiplying the availability, performance, and quality metrics, and then converting the result into a percentage.</p>
               <div class="math-equation">$$ \mathit{OEE} = \mathit{Availability} \times \mathit{Performance} \times \mathit{Quality} \times \mathit{100} $$</div><ul><li>Availability: Availability factor representing runtime as a share of scheduled time.</li><li>Performance: Performance factor representing actual production rate versus ideal rate.</li><li>Quality: Quality factor representing on-spec (good) output as a share of total output.</li><li>100: Value used in the calculation as defined by the code implementation.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>OEE is a key performance indicator used in various manufacturing and production environments to assess overall operational efficiency</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The inputs for calculating OEE include availability</li><li>performance</li><li>and quality metrics</li><li>which are derived from operational data</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>%</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for OEE is typically sourced from production logs, equipment sensors, and quality control reports.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>OEE is a vital tool for continuous improvement initiatives, as it highlights the effectiveness of equipment and processes in meeting production goals.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 3
   

      def calculate_overall_equipment_effectiveness(availability: float, performance: float, quality: float) -> float:
       """Calculates the OEE, a composite metric for manufacturing productivity."""
       # KPI: Overall Equipment Effectiveness (OEE)
       # Combines availability, performance, and quality to give a single measure of asset productivity.
       oee = availability * performance * quality * 100
       return oee