Flare Reduction %
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_04.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_04.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Flare%20Reduction%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Flare Reduction % measures the percentage decrease in gas flaring relative to the total gas produced</li><li>It is a critical indicator of operational efficiency and environmental performance in the oil and gas industry</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of Flare Reduction % is to minimize the volume of gas flared during production processes</li><li>thereby reducing greenhouse gas emissions and improving resource utilization</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The Flare Reduction % is calculated by taking the flare volume as a proportion of the total gas produced, subtracting this ratio from one, and then multiplying by one hundred to express it as a percentage.</p>
               <div class="math-equation">$$ \mathit{Flare\,Reduction\,\%} = \mathit{0)))} \times \mathit{100} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               49.2s (AI 49.2s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 49.245s
                  • AI: 49.245s
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
            <td><ul><li>This KPI is used in evaluating environmental performance</li><li>operational efficiency</li><li>and compliance with regulatory standards related to emissions</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the volume of gas flared and the total volume of gas produced</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Flare Reduction % is expressed as a percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is typically sourced from production reports and emissions monitoring systems within the organization.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher Flare Reduction % indicates better management of gas resources and a commitment to reducing environmental impact.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Flare Reduction %
   SELECT (1 - (flare_volume / NULLIF(total_gas,0))) * 100 AS [Flare Reduction %]
   FROM (SELECT 15.0 AS flare_volume, 100.0 AS total_gas) z;