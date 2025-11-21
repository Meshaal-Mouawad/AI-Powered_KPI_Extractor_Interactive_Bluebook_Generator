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
            <td><ul><li>Overall Equipment Effectiveness (OEE) is a key performance indicator that measures the efficiency and productivity of manufacturing equipment by evaluating its availability</li><li>performance</li><li>and quality output</li><li>Overall Equipment Effectiveness combines Availability</li><li>Performance</li><li>and Quality into a single effectiveness score</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of OEE is to provide a comprehensive assessment of equipment effectiveness</li><li>enabling organizations to identify areas for improvement and optimize production processes</li><li>Increase effective productive time by reducing downtime</li><li>speed losses</li><li>and quality losses</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>OEE is calculated by multiplying the availability, performance, and quality rates of equipment, expressed as a percentage.</p>
               <div class="math-equation">$$ \mathit{Oee\,\%} = \mathit{(Availability} \times \mathit{Performance} \times \mathit{Quality)} \times \mathit{100} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               49.9s (AI 49.9s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 49.862s
                  • AI: 49.862s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>100.0%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>0.0%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>OEE % is utilized in various KPIs related to production efficiency</li><li>equipment utilization</li><li>and operational performance</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for OEE include availability</li><li>performance</li><li>and quality metrics</li><li>which are derived from production data</li><li>Availability</li><li>performance</li><li>and quality factors calculated for the asset or line</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for OEE is a percentage, representing the proportion of effective production time relative to total available time.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>OEE data is typically sourced from manufacturing execution systems (MES), production logs, and equipment monitoring systems.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A high OEE percentage indicates that equipment is operating efficiently, while a low percentage suggests potential issues that may require investigation and corrective action.</td>
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