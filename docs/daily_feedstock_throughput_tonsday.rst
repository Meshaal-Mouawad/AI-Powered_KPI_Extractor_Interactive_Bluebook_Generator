Daily Feedstock Throughput (tons/day)
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:73" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=73" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Daily Feedstock Throughput measures the total volume of raw material that a petrochemical plant processes over a 24-hour period</li><li>It reflects the plant's operational efficiency and capacity utilization</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to assess the plant's ability to process feedstock effectively</li><li>ensuring that production targets are met while optimizing resource use</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The throughput is calculated by taking the total amount of feedstock processed in tons and dividing it by the number of hours the plant was operational, then multiplying by 24 to express it as a daily rate.</p>
               <div class="math-equation">$$ \mathit{Throughput} = \frac{\mathit{Total\,Feedstock\,Processed\,Tons}}{\mathit{Hours\,Online}} \times \mathit{24} $$</div><ul><li><i>Total Feedstock Processed Tons:</i> The numerator of the fraction.</li><li><i>Hours Online:</i> The denominator of the fraction.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in various operational assessments and can influence decisions related to production planning</li><li>resource allocation</li><li>and performance benchmarking</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measure for this KPI is the total feedstock processed in tons and the number of hours the plant has been online during the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>tons/day</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is typically sourced from the plant's operational logs and sensor data that track feedstock processing.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Monitoring Daily Feedstock Throughput is crucial for identifying trends in production capacity and for making informed decisions regarding maintenance and operational improvements.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 5
   

      def calculate_daily_throughput(total_feedstock_processed_tons: float, hours_online: float) -> float:
       """Calculates the average daily processing rate of the plant."""
       if hours_online == 0:
           return 0.0
       # KPI: Daily Feedstock Throughput (tons/day)
       # Measures the total volume of raw material the plant is processing over a 24-hour period.
       throughput = (total_feedstock_processed_tons / hours_online) * 24
       return throughput