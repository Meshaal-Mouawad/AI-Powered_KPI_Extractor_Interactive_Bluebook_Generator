OEE %
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/ax_kpi.dax:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/ax_kpi.dax&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=OEE%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Overall Equipment Effectiveness (OEE) is a key performance indicator that measures the efficiency and effectiveness of manufacturing equipment</li><li>It takes into account the availability</li><li>performance</li><li>and quality of the equipment in operation</li><li>Overall Equipment Effectiveness combines Availability</li><li>Performance</li><li>and Quality into a single effectiveness score</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of OEE is to provide a comprehensive view of how effectively a manufacturing operation is utilized</li><li>helping to identify areas for improvement and optimize production processes</li><li>Increase effective productive time by reducing downtime</li><li>speed losses</li><li>and quality losses</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>OEE is calculated by multiplying the availability, performance, and quality rates of the equipment, expressed as a percentage.</p>
               <div class="math-equation">$$ \mathit{Oee\,\%} = \mathit{(Availability} \times \mathit{Performance} \times \mathit{Quality)} \times \mathit{100} $$</div>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>OEE is commonly used in various KPIs related to production efficiency</li><li>equipment utilization</li><li>and operational performance in the oil</li><li>gas</li><li>and petrochemical industries</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for OEE include availability</li><li>performance</li><li>and quality rates</li><li>which are derived from operational data</li><li>Availability</li><li>performance</li><li>and quality factors calculated for the asset or line</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>OEE is expressed as a percentage, indicating the proportion of manufacturing time that is truly productive.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for OEE is typically sourced from production monitoring systems, equipment logs, and quality control reports.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A high OEE percentage indicates that equipment is being used effectively, while a low percentage suggests potential inefficiencies that need to be addressed.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: text
      :linenos:
   

      -- KPI: Overall Equipment Effectiveness (OEE)
   DEFINE MEASURE 'KPI'[OEE %] =
   VAR Availability = 0.95
   VAR Performance  = 0.98
   VAR Quality      = 0.99
   RETURN (Availability * Performance * Quality) * 100