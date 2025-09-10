Yield Percentage (%
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
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/plsql_kpi.pks:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/plsql_kpi.pks&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Yield%20Percentage%20%28%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Yield Percentage measures the efficiency of a production process by calculating the ratio of the desired product output to the total input used in the process</li><li>Proportion of desired product produced relative to total input</li><li>indicating conversion efficiency</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of tracking Yield Percentage is to assess and optimize production efficiency</li><li>ensuring that resources are utilized effectively to maximize output</li><li>Improve conversion efficiency and identify losses or off-spec production by trending yield over time</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The Yield Percentage is calculated by dividing the amount of desired product produced by the total input used, then multiplying the result by 100 to express it as a percentage.</p>
               <div class="math-equation">$$ \mathrm{Yield\,\%} = \frac{\mathrm{Desired\,Product}}{\mathrm{Total\,Input}} \times 100 $$</div>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>Yield Percentage is commonly used in key performance indicators related to production efficiency</li><li>resource utilization</li><li>and operational effectiveness in the oil</li><li>gas</li><li>and petrochemical industries</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measure consists of the total quantity of raw materials or resources consumed in the production process</li><li>Desired product output and corresponding input over the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Yield Percentage is expressed as a percentage (%).</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for Yield Percentage is typically sourced from production reports, operational databases, and performance monitoring systems.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher Yield Percentage indicates a more efficient production process, while a lower percentage may signal issues such as waste, inefficiencies, or suboptimal resource allocation.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Yield Percentage (%)
   -- Formula: \mathrm{Yield\,\%} = \frac{\mathrm{Desired\,Product}}{\mathrm{Total\,Input}} \times 100

   CREATE OR REPLACE PACKAGE kpi_pkg AS
     FUNCTION yield_pct(desired_product NUMBER, total_input NUMBER) RETURN NUMBER;